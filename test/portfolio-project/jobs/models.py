from django.db import models

class Job(models.Model):
    summary = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
