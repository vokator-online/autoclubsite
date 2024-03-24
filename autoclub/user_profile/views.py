from django.views import generic
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from . import forms
from user_profile.models import Profile



class UserRegisterView(generic.CreateView):
    form_class = forms.CreateUserForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


class ShowProfilePageView(generic.DetailView):
    model = Profile
    template_name = 'user_profile/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context


class UserEditView(generic.UpdateView):
    form_class = forms.EditProfileForm
    template_name = 'user_profile/edit_profile.html'
    success_url = reverse_lazy('discussion')

    def get_object(self):
        return self.request.user


class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class = forms.ProfilePageForm
    template_name = 'user_profile/edit_profile_page.html'
    success_url = reverse_lazy('discussion')



class PasswordsChangeView(PasswordChangeView):
    success_url = reverse_lazy('password_success')
    template_name = 'registration/password_change_done.html'
