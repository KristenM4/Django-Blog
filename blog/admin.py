from django.contrib import admin

# Register your models here.

from .models import Author, Tag, Post


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email_address",)


class TagAdmin(admin.ModelAdmin):
    list_display = ("caption",)


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date", "excerpt", "image_name", "slug", "content")
    list_filter = ("author", "tags",)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
