from django.db import models

# Create your models here.
class Agent(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    short_note = models.TextField(max_length=500)
    profile_img = models.ImageField(upload_to='photos/agents/%Y/%m/%d/', blank=True)
    facebook = models.URLField(max_length=200, blank=True)
    twitter = models.URLField(max_length=200, blank=True)
    linkedIn = models.URLField(max_length=200, blank=True)
    email = models.EmailField(max_length=254)
    is_mvp = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    