from django.db import models

# Create your models here.

class Upload(models.Model):

    Logo = models.ImageField(upload_to='post_images')

