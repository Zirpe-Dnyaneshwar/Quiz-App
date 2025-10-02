from django.db import models

# Create your models here.

from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=1255)
    option1 = models.CharField(max_length=1000)
    option2 = models.CharField(max_length=1000)
    option3 = models.CharField(max_length=1000)
    option4 = models.CharField(max_length=1000)
    correct_answer = models.CharField(max_length=1000)

    def __str__(self):
        return self.question_text
