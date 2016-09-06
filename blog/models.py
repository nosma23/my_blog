from __future__ import unicode_literals
from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models
from django.db.models import permalink
from django.utils.safestring import mark_safe
from markdown_deux import markdown


class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(null=True, blank=True,
                              width_field='width_field',
                              height_field='height_field')
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    body = RichTextField()
    publish = models.DateTimeField(auto_now=False, auto_now_add=False)
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.Category')

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

    def get_markdown(self):
        body = self.body
        return mark_safe(markdown(body))


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })




