from django.db import models

class UserDetails(models.Model):
    email = models.EmailField(unique=True)
    dob = models.DateField()
    age = models.CharField(max_length=10)
    password = models.CharField(max_length=25)