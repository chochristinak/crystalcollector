from django.db import models
from django.urls import reverse
REASONS = (
    ('H', 'Health'),
    ('E', 'Emotional'),
    ('S', 'Spiritual'),
    ('C', 'Career'),
)
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
       
class Reading(models.Model):
    date = date = models.DateField('reading date')
    reason = models.CharField(
        max_length=50,
        choices = REASONS)
    crystal = models.ForeignKey(Crystal, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_reason_display()} on {self.date}"
   