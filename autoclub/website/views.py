from django.views.generic import TemplateView
from typing import Any
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.views import generic
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.shortcuts import redirect
from . import models, forms, utils


class HomeView(TemplateView):
    template_name = 'main/home.html'


class EventsView(TemplateView):
    template_name = 'main/events.html'


class CinemaView(TemplateView):
    template_name = 'main/cinema.html'


class MeetingsView(TemplateView):
    template_name = 'main/meetings.html'


class ApplicationsView(TemplateView):
    template_name = 'main/applications.html'


class MerchandiseView(TemplateView):
    template_name = 'main/merchandise.html'


class TicketCreateView(generic.CreateView):
    model = models.Ticket
    template_name = 'main/contact.html'

    def get_form_class(self) -> type[BaseModelForm]:
        if self.request.user.is_authenticated:
            return forms.TicketFormUser
        else:
            return forms.TicketFormGuest

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.sender = self.request.user
            form.instance.clean()
        self.obj:models.Ticket = form.instance
        return super().form_valid(form)

    def get_success_url(self) -> str:
        utils.send_support_ticket_email(self.request, self.obj)
        return reverse_lazy('home')


class TicketDetail(UserPassesTestMixin, generic.edit.FormMixin, generic.DetailView):
    model = models.Ticket
    template_name = 'customer_support/ticket_detail.html'
    form_class = forms.TicketMessageForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        ticket:models.Ticket = self.object
        form.instance.ticket = ticket
        form.instance.recipient_email = settings.ADMIN_EMAIL
        form.instance.recipient_name = settings.ADMIN_NAME
        if self.request.user.is_authenticated:
            form.instance.sender = self.request.user
            form.instance.clean()
        else:
            form.instance.sender_name = ticket.sender_name
            form.instance.sender_email = ticket.sender_email
        form.save()
        utils.send_support_ticket_email(self.request, form.instance)
        return redirect(f"{reverse_lazy('ticket_detail', kwargs={'pk':ticket.pk})}?access_key={ticket.access_key}")

    def test_func(self) -> bool | None:
        obj = self.get_object()
        if self.request.user.is_authenticated and obj.sender == self.request.user:
            return True
        else:
            if not obj.sender and obj.access_key == self.request.GET.get('access_key'):
                return True
        return False


class TicketList(LoginRequiredMixin, generic.ListView):
    model = models.Ticket
    template_name = 'customer_support/ticket_list.html'

    def get_queryset(self) -> QuerySet[Any]:
        qs = super().get_queryset()
        qs = qs.filter(sender=self.request.user)
        return qs
    

class GrandView(TemplateView):
    template_name = 'main/grand_meet_2023.html'
