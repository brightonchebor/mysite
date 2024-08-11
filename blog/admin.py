from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin

# Register your models here.
"""
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title','status','slug','author')
    
admin.site.register(models.Post, AuthorAdmin)
"""

@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):

    list_display = ("title", "id", "status", "slug", "author")
    prepopulated_fields = {
        "slug": ("title",),
    }

admin.site.register(models.Comment, MPTTModelAdmin)


admin.site.register(models.Category)
    