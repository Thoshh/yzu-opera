# -*- coding: utf-8 -*-

from django.contrib import admin
from models import *

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['owner', 'website', 'avatar', 'date']
    
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['owner', 'description', 'date']

class EntryAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'date']
    prepopulated_fields = {
        'slug': ('title',)
    }

class CommentAdmin(admin.ModelAdmin):
    list_display = ['entry', 'cmt', 'author', 'date']

class LinksAdmin(admin.ModelAdmin):
    list_display = ['name', 'website', 'description', 'date']

admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Links, LinksAdmin)
