from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import AutoCreatedUpdatedModel

USER = get_user_model()


class BaseBlogModel(models.Model):
    class Meta:
        abstract = True

    is_published = models.NullBooleanField(default=False)


class Category(AutoCreatedUpdatedModel, BaseBlogModel):
    name = models.CharField(max_length=255, null=True, blank=True, help_text=_('카테고리'))


class Post(AutoCreatedUpdatedModel, BaseBlogModel):
    categories = models.ManyToManyField(Category, related_name='posts')
    author = models.ForeignKey(USER, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True, help_text=_('글 제목'))
    body = models.TextField(null=True, blank=True, help_text=_('글 내용'))


class Comment(AutoCreatedUpdatedModel, BaseBlogModel):
    author = models.ForeignKey(USER, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True, help_text=_('글 내용'))
