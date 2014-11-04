from django.db import models

# Create your models here.
class Temperature(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)
    value = models.FloatField('value in C')
