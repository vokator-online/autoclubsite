from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from user_profile.models import Profile


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'custom-form-control', 'placeholder': 'Please enter your First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'custom-form-control', 'placeholder': 'Please enter your Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'custom-form-control', 'placeholder': 'Please enter your e-mail address'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Username:'
        self.fields['username'].widget.attrs.update({'placeholder': 'Please enter username'})
        self.fields['first_name'].label = 'First Name:'
        self.fields['last_name'].label = 'Last Name:'
        self.fields['email'].label = 'Email:'
        self.fields['password1'].label = 'Password:'
        self.fields['password1'].widget.attrs.update({'placeholder': 'Please enter the password you created'})
        self.fields['password2'].label = 'Password confirmation:'
        self.fields['password2'].widget.attrs.update({'placeholder': 'Please enter the password you created and confirm'})


class ProfilePageForm(forms.ModelForm):
    bio = forms.CharField(
        label=_('Bio'), 
        widget=forms.Textarea(attrs={'class': 'custom-form-control', 'placeholder': _('Please tell us more about yourself')}),
        required=False
    )
    website_url = forms.CharField(
        label=_('Website url'),
        widget=forms.TextInput(attrs={'class': 'custom-form-control', 'placeholder': _('Your website page (if you have one)')}),
        required=False
    )
    facebook_url = forms.CharField(
        label=_('Facebook url'),
        widget=forms.TextInput(attrs={'class': 'custom-form-control', 'placeholder': _('Your Facebook page (if you have one)')}),
        required=False
    )
    twitter_url = forms.CharField(
        label=_('Twitter url'),
        widget=forms.TextInput(attrs={'class': 'custom-form-control', 'placeholder': _('Your Twitter page (if you have one)')}),
        required=False
    )
    instagram_url = forms.CharField(
        label=_('Instagram url'),
        widget=forms.TextInput(attrs={'class': 'custom-form-control', 'placeholder': _('Your Instagram page (if you have one)')}),
        required=False
    )
    pinterest_url = forms.CharField(
        label=_('Pinterest url'),
        widget=forms.TextInput(attrs={'class': 'custom-form-control', 'placeholder': _('Your Pinterest page (if you have one)')}),
        required=False
    )

    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url')


class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        label=_('First Name'),
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'custom-form-control', 'placeholder': _('Please enter your First Name')})
    )
    last_name = forms.CharField(
        label=_('Last Name'),
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'custom-form-control', 'placeholder': _('Please enter your Last Name')})
    )
    email = forms.EmailField(
        label=_('Email'),
        widget=forms.EmailInput(attrs={'class': 'custom-form-control', 'placeholder': _('Please enter your e-mail address')})
    )
    last_login = forms.CharField(
        label=_('Last login'),
        max_length=100,
        widget=forms.TextInput(attrs={'readonly': True})
    )
    date_joined = forms.CharField(
        label=_('Date joined'),
        max_length=100,
        widget=forms.TextInput(attrs={'readonly': True})
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'last_login', 'date_joined')
