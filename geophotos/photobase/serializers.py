from rest_framework import serializers
from photobase.models import SiteDoc, Image
from django.contrib.auth.models import User

class SiteDocSerializer(serializers.Serializer):
    house_number = serializers.IntegerField()
    street = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    zip_code = serializers.IntegerField()

    name = serializers.CharField()
    site_plan = serializers.ImageField()
    floor = serializers.IntegerField(required=False)

     # geo data
    upperleft_geo_x = serializers.DecimalField(decimal_places=16, max_digits=21)
    upperleft_geo_y = serializers.DecimalField(decimal_places=16, max_digits=21)
    bottomright_geo_x = serializers.DecimalField(decimal_places=16, max_digits=21)
    bottomright_geo_y = serializers.DecimalField(decimal_places=16, max_digits=21)

    # pixel data
    upperleft_pix_x = serializers.DecimalField(decimal_places=16, max_digits=21)
    upperleft_pix_y = serializers.DecimalField(decimal_places=16, max_digits=21)
    bottomright_pix_x = serializers.DecimalField(decimal_places=16, max_digits=21)
    bottomright_pix_y = serializers.DecimalField(decimal_places=16, max_digits=21)


class ImageSerializer(serializers.Serializer):
    # title
    title = serializers.CharField()

    # geo location
    geo_x = serializers.DecimalField(decimal_places=16, max_digits=21)
    geo_y = serializers.DecimalField(decimal_places=16, max_digits=21)

    # user tagging
    tags = serializers.MultipleChoiceField(choices=[str(_) for _ in User.objects.all()])

    # image data
    image = serializers.ImageField()
    note = serializers.CharField(allow_blank=True)
    flag = serializers.IntegerField()
