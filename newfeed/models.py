from django.db import models

# Create your models here.
class Newfeed(models.Model):
    title = models.CharField(max_length=100)
    discription = models.CharField(max_length=300)
    image = models.ImageField(upload_to='newfeed/image/')
    url = models.URLField(blank=True)
