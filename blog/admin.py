from django.contrib import admin
from . import models

# Register your models here.
"""
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title','status','slug','author')
    
admin.site.register(models.Post, AuthorAdmin)
"""

@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):

    list_display = ("title", "status", "slug", "author")
    prepopulated_fields = {
        "slug": ("title",),
    }


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ("post", "name", "email", "publish", "status")
    list_filter = ("status", "publish")
    search_fields = ("name", "email", "comment")

admin.site.register(models.Category)
    