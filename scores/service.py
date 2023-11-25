from scores.models import Score, AverageScore


class ScoreService:
    @staticmethod
    def get_score(user_id: int, post_id: int) -> Score:
        return Score.objects.filter(user_id=user_id, post_id=post_id).first()

    @staticmethod
    def _average_score(post_id: int) -> AverageScore:
        average = AverageScore.objects.filter(post_id=post_id).first()
        if not average:
            average = AverageScore(post_id=post_id, score=0, number=0)
        return average

    @classmethod
    def get_average_score(cls, post_id: int) -> (int, int):
        average_score = cls._average_score(post_id)
        return average_score.score, average_score.number

    @classmethod
    def add_score_to_average(cls, post_id: int, new_score: int) -> (int, int):
        average_score = cls._average_score(post_id)
        new_number = average_score.number + 1
        new_average_score = (
            average_score.score * average_score.number + new_score
        ) / new_number
        average_score.number = new_number
        average_score.score = new_average_score
        average_score.save()
        return average_score.score, average_score.number

    @classmethod
    def update_score_in_average(
        cls, post_id: int, old_score: int, new_score: int
    ) -> (int, int):
        average_score = cls._average_score(post_id)
        old_sum = average_score.score * average_score.number
        new_sum = old_sum + new_score - old_score
        average_score.score = new_sum / average_score.number
        average_score.save()
        return average_score.score, average_score.number
