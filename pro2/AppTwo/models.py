from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=20,unique=False)
    last_name = models.CharField(max_length=20,unique=False)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.first_name  