from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    average_score = serializers.FloatField(source="average_score.score", read_only=True)
    scores_number = serializers.FloatField(
        source="average_score.number", read_only=True
    )

    class Meta:
        model = Post
        read_only_fields = (
            "id",
            "average_score",
            "scores_number",
            "created_at",
            "updated_at",
        )
        fields = (
            "id",
            "title",
            "author",
            "content",
            "created_at",
            "updated_at",
            "average_score",
            "scores_number",
        )
