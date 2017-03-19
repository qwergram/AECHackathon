from django.db import models
from django.contrib.auth.models import User
from geophotos import settings

# Create your models here.

class Image(models.Model):
    # TimeStamp
    time_created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    by = models.ManyToManyField(User, related_name='images')
    
    title = models.CharField(max_length=255, unique=True)

    # geo location
    geo_x = models.DecimalField(decimal_places=16, max_digits=21)
    geo_y = models.DecimalField(decimal_places=16, max_digits=21)

    # user tagging
    tags = models.ManyToManyField(User)

    # image data
    image = models.ImageField(upload_to='dcim/')
    note = models.TextField()
    flag = models.IntegerField()


class SiteDoc(models.Model):
    # TimeStamp
    time_created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    by = models.ManyToManyField(User)

    # Address
    house_number = models.IntegerField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField()

    # site plan data
    name = models.CharField(max_length=255, unique=True)
    location = models.ForeignKey(Location)
    site_plan = models.ImageField(upload_to='sites/')
    floor = models.IntegerField()

    # geo data
    upperleft_geo_x = models.DecimalField(decimal_places=16, max_digits=21)
    upperleft_geo_y = models.DecimalField(decimal_places=16, max_digits=21)
    bottomright_geo_x = models.DecimalField(decimal_places=16, max_digits=21)
    bottomright_geo_y = models.DecimalField(decimal_places=16, max_digits=21)

    # pixel data
    upperleft_pix_x = models.DecimalField(decimal_places=16, max_digits=21)
    upperleft_pix_y = models.DecimalField(decimal_places=16, max_digits=21)
    bottomright_pix_x = models.DecimalField(decimal_places=16, max_digits=21)
    bottomright_pix_y = models.DecimalField(decimal_places=16, max_digits=21)

    # images
    photos = models.ManyToManyField(Image)









