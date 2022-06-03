from django.db import models

# Create your models here.

class Movie(models.Model):
  num = models.IntegerField()
  title = models.CharField(max_length=30)
  overview = models.CharField(max_length=200)
  poster = models.ImageField(upload_to='images/',default='image')
  vote_average = models.IntegerField()
  vote_count = models.IntegerField()
  
  def __str__(self):
    return self.title
  
  def save_movie(self):
    self.save()
  
