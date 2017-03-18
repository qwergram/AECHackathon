from django.db import models
from django.contrib.auth.models import User
from geophotos import settings

# Create your models here.



class Location(models.Model):
    # TimeStamp
    time_created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    by = models.ManyToManyField(User)

    # address
    house_number = models.IntegerField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField()


class Coords(models.Model):
    # TimeStamp
    time_created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    by = models.ManyToManyField(User)

    # coordinates
    address = models.ForeignKey(Location)
    x = models.DecimalField(decimal_places=16, max_digits=21)
    y = models.DecimalField(decimal_places=16, max_digits=21)
    floor = models.IntegerField()


class SitePlan(models.Model):
    # TimeStamp
    time_created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    by = models.ManyToManyField(User)
    
    # pdf data
    # populate with an external link
    external = models.CharField(max_length=255, unique=True)
    # convert to image when needed
    image = models.ImageField(upload_to=settings.MEDIA_ROOT + 'sites/')
    

class SiteDoc(models.Model):
    # TimeStamp
    time_created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    by = models.ManyToManyField(User)

    location = models.ForeignKey(Location)
    site_plan = models.ManyToManyField(SitePlan)

class Image(models.Model):
    # TimeStamp
    time_created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    by = models.ManyToManyField(User, related_name='images')
    
    # data
    image = models.ImageField(upload_to=settings.MEDIA_ROOT + 'dcim/')
    geo = models.ForeignKey(Coords)
    note = models.TextField()
    flag = models.IntegerField()
    tags = models.ManyToManyField(User)






