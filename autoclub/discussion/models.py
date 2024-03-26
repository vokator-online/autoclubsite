from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from tinymce.models import HTMLField


CATEGORY_CHOICES = (
    ('', _('Please Choose a Topic That Interests You')),
    ('Meetings', _('Meetings and Joint Activities')),
    ('Event', _('Event Overview and Organizational Issues')),
    ('Cinema', _('Going to the Cinema')),
    ('Suggestions', _('Suggestions for Club Activities')),
    ('Introduction', _('New Members Introduction')),
    ('Discussions', _('General Discussions (Off Topic)')),
    ('Testing', _('Testing Environment')),
)


class Category(models.Model):
    name = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default='')

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("discussion")


class Post(models.Model):
    title = models.CharField(_("title"), max_length=255)
    header_image = models.ImageField(_("header image"), upload_to='images/', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name=_("author"), related_name='posts', on_delete=models.CASCADE, db_index=True)
    content = HTMLField(verbose_name=_("content"))
    snippet = models.CharField(_("snippet"), max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True, db_index=True)
    category = models.ForeignKey(Category, verbose_name=_("category"), related_name='posts', on_delete=models.CASCADE, null=True, db_index=True)

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")
        ordering = ['-created_at']

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, verbose_name=_("post"), related_name='comments', on_delete=models.CASCADE, db_index=True)
    author = models.ForeignKey(User, verbose_name=_("author"), related_name='user_comments', on_delete=models.CASCADE, null=True, db_index=True)
    content = HTMLField(verbose_name=_("content"))
    created_at = models.DateTimeField(_("created at"), auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True, db_index=True)
    
    class Meta:
        verbose_name = _("comment")
        verbose_name_plural = _("comments")
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.post.title} | {self.author.username}'

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.post.pk})
