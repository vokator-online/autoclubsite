from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("discussion")


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("title"))
    header_image = models.ImageField(null=True, blank=True, upload_to="images/", verbose_name=_("header image"))
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, verbose_name=_("author"))
    content = HTMLField(verbose_name=_("content"))
    snippet = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("snippet"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated at"))
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE, null=True, verbose_name=_("category"))

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")
        ordering = ['-created_at']

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})
    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, verbose_name=_("post"))
    author = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE, null=True, verbose_name=_("author"))
    content = HTMLField(verbose_name=_("content"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated at"))
    
    class Meta:
        verbose_name = _("comment")
        verbose_name_plural = _("comments")
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.post.title} | {self.author.username}'

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.post.pk})
    