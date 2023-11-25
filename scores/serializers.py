from rest_framework import serializers

from scores.models import Score


class ScoreSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Score
        fields = ("score_number", "user", "post_id")

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        data["post_id"] = int(self.context["request"].parser_context["kwargs"]["pk"])
        return data
