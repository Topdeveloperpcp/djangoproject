from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    Name       = models.CharField(max_length = 200)
    Address    = models.CharField(max_length = 300)
    Pan_No     = models.CharField(max_length = 100)
    Regd_No    = models.CharField(max_length = 100)
    Telephone  = models.CharField(max_length = 300)
    Mobile     = models.CharField(max_length = 300)
    Email      = models.CharField(max_length = 300)
    Web        = models.CharField(max_length = 300)
    State      = models.CharField(max_length = 300)
    Country    = models.CharField(max_length = 300)
    Created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    Logo       = models.ImageField(upload_to='post_images')

    def __str__(self):
        return self.Name