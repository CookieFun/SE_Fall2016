from django.contrib import admin

# Register your models here.

from .models import Column, Event


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'info', 'nav_display', 'home_display')


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'pub_time', 'upd_time', 'vis_count')


admin.site.register(Column, ColumnAdmin)
admin.site.register(Event, EventAdmin)
