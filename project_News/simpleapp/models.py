from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime


class News_Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name.title()}'



class News(models.Model):
    title = models.CharField(max_length=100, unique=True)
    text = models.TextField()
    category = models.ForeignKey(to='News_Category', on_delete=models.CASCADE, related_name='news')
    date_time_in = models.DateTimeField('дата публикации', auto_now_add=True)

    def __str__(self):
        return f'{self.title.title()}: {self.text[:150]}'