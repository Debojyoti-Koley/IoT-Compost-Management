from django.db import models

# Create your models here.


class Compost(models.Model):
    Date_of_add = models.DateField()
    Uid = models.TextField()
    Temp = models.FloatField()
    Humidity = models.FloatField()
