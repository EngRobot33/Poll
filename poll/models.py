from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=256)
    published_date = models.DateTimeField(default=timezone.now,)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 256)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text
