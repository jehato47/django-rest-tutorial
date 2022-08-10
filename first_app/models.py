from django.db import models


# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100)
    note = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
