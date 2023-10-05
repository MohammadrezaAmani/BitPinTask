from django.db import models
from django.contrib.auth.models import User


class Content(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return f"{self.id} - {self.title} - {self.average_rating} - {self.number_of_ratings} - {self.user_rating}"

    @property
    def average_rating(self):
        sum = 0
        ratings = Rating.objects.filter(content=self)
        for rating in ratings:
            sum += rating.score
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0

    @property
    def number_of_ratings(self):
        ratings = Rating.objects.filter(content=self)
        return len(ratings)

    @property
    def user_rating(self):
        ratings = Rating.objects.filter(content=self)
        user = User.objects.first()
        for rating in ratings:
            if rating.user == user:
                return rating.score
        return 0

    def __repr__(self) -> str:
        return self.title


SCORE_CHOICES = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    score = models.IntegerField(choices=SCORE_CHOICES)

    class Meta:
        unique_together = ["user", "content"]

    def __str__(self):
        return f"{self.user} - {self.content} - {self.score}"

    def __repr__(self) -> str:
        return f"{self.user} - {self.content} - {self.score}"

    @property
    def user_ratings(self):
        return Rating.objects.filter(user=self.user)
