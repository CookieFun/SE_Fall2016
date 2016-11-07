# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible

from django.core.urlresolvers import reverse


# Create your models here.
@python_2_unicode_compatible
class Column(models.Model):
    name = models.CharField('栏目名', max_length=256)
    slug = models.CharField('栏目网址', max_length=256, db_index=True)

    def get_absolute_url(self):
        return reverse('column', args=(self.slug,))

    info = models.TextField('栏目信息', default='')

    home_display = models.BooleanField('首页显示', default=False)
    nav_display = models.BooleanField('导航显示', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '栏目'
        verbose_name_plural = '栏目'
        ordering = ['name']


@python_2_unicode_compatible
class Event(models.Model):
    # id 这个是默认有的，也可以自己定义一个其它的主键来覆盖它
    id = models.AutoField(primary_key=True)
    column = models.ManyToManyField(Column, verbose_name='归属栏目')
    title = models.CharField('标题', max_length=256)
    slug = models.CharField('网址', max_length=256, db_index=True)

    def get_absolute_url(self):
        return reverse('event', args=(self.id, self.slug,))

    author = models.CharField('作者', max_length=256, blank=True)
    content = models.TextField('内容', default='', blank=True)
    pub_time = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    upd_time = models.DateTimeField('更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '事件'
        verbose_name_plural = '事件'
