from scores.models import Score


class ScoreService:
    @staticmethod
    def get_score(user_id, post_id):
        return Score.objects.filter(user_id=user_id, post_id=post_id).first()
