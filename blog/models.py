import datetime

from django.db import models
from django.utils import timezone

class Category(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField(max_length=200)
    pub_date = models.DateTimeField('date published')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

