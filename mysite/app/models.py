from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200, blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=200, blank=True)
    testType = models.CharField(max_length=200, blank=True)
    testAtime = models.CharField(blank=True, max_length=200)
    question1 = models.CharField(max_length=200, blank=True)
    question2 = models.CharField(max_length=200, blank=True)
    question3 = models.CharField(max_length=200, blank=True)
    testBtime = models.CharField(blank=True, max_length=200)
    question4 = models.CharField(max_length=200, blank=True)
    question5 = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name