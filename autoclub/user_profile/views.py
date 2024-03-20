from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from . import forms
from user_profile.models import Profile



class UserRegisterView(generic.CreateView):
    form_class = forms.CreateUserForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


# def signup(request: HttpRequest) -> HttpResponse:
#     if request.method == "POST":
#         form = forms.UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = forms.UserCreationForm()
#     return render(request, 'registration/registration.html', {
#         'form': form,
#     })


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
    template_name = 'user_profile/edit_profile_page.html'
    fields = ['bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url']
    success_url = reverse_lazy('discussion')


class PasswordsChangeView(PasswordChangeView):
    success_url = reverse_lazy('password_success')
    template_name = 'registration/password_change_done.html'
    