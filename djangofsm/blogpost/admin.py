from django.contrib import admin

from django_fsm_log.admin import StateLogInline

from blogpost.models import BlogPost

# Register your models here.
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    inlines = [StateLogInline]
    list_display = ["title", "state"]
