# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible

from django.core.urlresolvers import reverse

from DjangoUeditor.models import UEditorField

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
    slug = models.CharField('网址', max_length=256, db_index=True, default='event')

    def get_absolute_url(self):
        return reverse('event', args=(self.id, self.slug,))

    event_time = models.DateTimeField('时间', editable=True, null=True, blank=True)
    place = models.CharField('地点', max_length=256, blank=True)
    speaker = models.CharField('嘉宾', max_length=256, blank=True)
    
    author = models.CharField('作者', max_length=256, blank=True)
    abstract = models.CharField('简介', max_length=256, blank=True)
    content = UEditorField('内容', height=300, width=1000,
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='besttome', filePath='uploads/files/')

    pub_time = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    upd_time = models.DateTimeField('更新时间', auto_now=True, null=True)

    vis_count = models.IntegerField('访问次数', default=0, editable=False)

    def get_month(self):
        mon = {1: 'Jan', 2: 'Feb', 3: 'Mat', 4: 'Apr', 5: 'May', 6: 'Jun',
               7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
        return mon[self.pub_time.month]

    def visit(self):
        self.vis_count=self.vis_count+1
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '事件'
        verbose_name_plural = '事件'
        ordering = ['-pub_time']
