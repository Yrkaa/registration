from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    ip = models.CharField(max_length=500000)

    def __str__(self):
        return self.name