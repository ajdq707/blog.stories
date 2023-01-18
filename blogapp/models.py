from django.db import models
from django.utils.datetime_safe import date


# Create your models here.

class postdb(models.Model):
    title = models.CharField(max_length=200)
    titlesub = models.TextField()
    postdate = models.DateField(default=date.today, blank=False, null=False)
    authorname = models.TextField()
    author_image = models.ImageField(upload_to='images')
    postimage = models.ImageField(upload_to='images')
    postcontent = models.TextField()

class postab(models.Model):
    about=models.TextField()

class sidepost(models.Model):
    imageside=models.ImageField(upload_to='images')
    dateside=models.TextField()
    headsub=models.TextField()
    story=models.TextField()

class aboutme(models.Model):
    Name=models.CharField(max_length=50)
    subname=models.CharField(max_length=25)
    myimg=models.ImageField(upload_to='images')
    thumbnail=models.ImageField(upload_to='images')
