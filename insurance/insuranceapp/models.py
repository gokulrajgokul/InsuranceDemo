from django.db import models

class UserData(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=15)   # use CharField for flexibility
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
