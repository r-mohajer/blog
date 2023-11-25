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
