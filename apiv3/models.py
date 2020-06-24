from django.db import models

# Create your models here.

class UserApis(models.Model):
    name = models.CharField(unique=False, max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(unique=False, max_length=50)

    def __str__(self):
        return self.name
