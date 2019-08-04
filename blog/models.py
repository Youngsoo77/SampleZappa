from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.translation import gettext_lazy as _

from base.models import AutoCreatedUpdatedModel

USER = get_user_model()


class BaseBlogModel(models.Model):
    class Meta:
        abstract = True

    is_published = models.NullBooleanField(default=False)


class Category(AutoCreatedUpdatedModel, BaseBlogModel):
    name = models.CharField(max_length=255, null=True, blank=True, help_text=_('카테고리'))

    def __str__(self):
        return self.name if self.name else "empty name"


class Post(AutoCreatedUpdatedModel, BaseBlogModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(USER, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True, help_text=_('글 제목'))
    body = models.TextField(null=True, blank=True, help_text=_('글 내용'))

    def __str__(self):
        return f"[{self.category}] {self.title if self.title else ''}"


class Comment(AutoCreatedUpdatedModel, BaseBlogModel):
    author = models.ForeignKey(USER, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True, help_text=_('글 내용'))

    @property
    def short_body(self):
        return truncatechars(self.body, 20) if self.body else ""

    def __str__(self):
        return f"{self.short_body} ({self.author.username})"
