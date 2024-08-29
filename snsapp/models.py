from django.db import models

# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    author = models.CharField(max_length=20)
    thumbnail = models.ImageField(upload_to='')
    good = models.IntegerField(null=True, blank=True, default=1)
    read = models.IntegerField(null=True, blank=True, default=1)
    readname = models.TextField(null=True, blank=True, default='')