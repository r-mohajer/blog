from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Score(models.Model):
    score_number = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.user.username + " " + str(self.post) + ": " + str(self.score_number)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_or_update_initial_values()

    def set_or_update_initial_values(self):
        self.initial_values = {
            "score_number": self.score_number,
        }


class AverageScore(models.Model):
    score = models.FloatField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    number = models.IntegerField(default=1)
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.post) + ": " + str(self.score)
