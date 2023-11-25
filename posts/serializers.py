from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        readonly_fields = (
            "author",
            "created_at",
            "updated_at",
        )
        fields = (
            "title",
            "author",
            "content",
            "created_at",
            "updated_at",
        )
