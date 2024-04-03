from django.db import models
from django.urls import reverse

# Create your models here.

class Crystal(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    properties = models.TextField(max_length=250)
    shakra = models.CharField(max_length=50)
    mohs = models.IntegerField()
    image = models.URLField(blank=True)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'crystal_id': self.id})
       

       