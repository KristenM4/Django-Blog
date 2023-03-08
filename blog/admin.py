from django.contrib import admin

# Register your models here.

from .models import Author, Tag, Post, Comment


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email_address",)


class TagAdmin(admin.ModelAdmin):
    list_display = ("caption",)


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date", "excerpt", "image_name", "slug", "content")
    list_filter = ("author", "tags",)
    prepopulated_fields = {"slug": ("title",)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "date", "comment_content", "blog_post")
    list_filter = ("blog_post", "user_name", "date")

admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)