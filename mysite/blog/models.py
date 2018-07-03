from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Post(models.Model):
    TABLE_OF_CHOICES = (('draft','Roboczy'),('published','Opublikowany'),)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    body_text = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length = 20, choices= TABLE_OF_CHOICES, default = 'draft'  )
    avr_score = models.DecimalField(max_digits=3, decimal_places=1)

    def published(self):
        self.publish = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Score(models.Model):
    PostScore = models.ForeignKey(Post,on_delete=models.CASCADE)
    value = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
