from django.db import models

# Create your models here.


class Data(models.Model):
    # sentiment = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    word = models.TextField(max_length=100)
    count = models.IntegerField()
