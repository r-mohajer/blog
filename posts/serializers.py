from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        read_only_fields = (
            # "author",
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
