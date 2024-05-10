from django import forms
from .models import Post, Category, Comment
from django.utils.translation import gettext_lazy as _


# choices = Category.objects.all().values_list('name', 'name')

# choice_list = []

# for item in choices:
#     choice_list.append(item)


class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label=_('Please Choose a Topic That Interests You'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Post
        fields = ('title', 'category', 'content', 'header_image', 'snippet')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Please Enter the Title of the Post')}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'placeholder': _('You Can Leave a Fragment of the Message Here')}),
        }


class EditForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label=_('Please Choose a Topic That Interests You'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Post
        fields = ('title', 'category', 'content', 'header_image', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Please Enter the Title of the Post')}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'placeholder': _('You Can Leave a Fragment of the Message Here')}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
