from django.contrib import admin
from posts.models import Post


@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "content",
        "created_at",
        "updated_at",
    )
