from django.views.generic import TemplateView
from django.forms.models import BaseModelForm
from django.views import generic
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
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
        return reverse_lazy('index')
    