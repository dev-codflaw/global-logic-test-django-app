from django.db import models

# Create your models here.



class Answer(models.Model):
    option1 = models.CharField(max_length=500)
    option2 = models.CharField(max_length=500)
    option3 = models.CharField(max_length=500)
    option4 = models.CharField(max_length=500)


class Question(models.Model):
    que_txt = models.CharField(max_length=250)
    ans = models.ManyToManyField(Answer)

    def __str__(self):
        return self.que_txt