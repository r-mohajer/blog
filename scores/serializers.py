from rest_framework import serializers

from scores.models import Score
from scores.service import ScoreService


class ScoreSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Score
        fields = ("score_number", "user", "post_id")

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        data["post_id"] = int(self.context["request"].parser_context["kwargs"]["pk"])
        return data

    def update(self, instance, validated_data):
        score = ScoreService().get_score(
            validated_data["user"].id, validated_data["post_id"]
        )
        return super().update(score, validated_data)
