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

    def create(self, validated_data):
        instance = super().create(validated_data)
        ScoreService().add_score_to_average(
            validated_data["post_id"], new_score=validated_data["score_number"]
        )
        return instance

    def update(self, instance, validated_data):
        post_id = validated_data["post_id"]
        score = ScoreService().get_score(validated_data["user"].id, post_id)
        old_score = score.score_number
        new_instance = super().update(score, validated_data)
        ScoreService().update_score_in_average(
            post_id, old_score, new_score=validated_data["score_number"]
        )
        return new_instance
