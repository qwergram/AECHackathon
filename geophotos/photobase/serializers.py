from rest_framework import serializers
from photobase.models import Location, Coords, SitePlan, SiteDoc, Image

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('house_number', 'street', 'city', 'state', 'zip_code')


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ('address', 'x', 'y', 'floor')

class SitePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SitePlan
        fields = ('external', )

    image = serializers.ImageField(required=False)


class SiteDocSerializer(serializers.Serializer):
    location = serializers.CharField()
    site_plan = serializers.CharField()


class ImageSerializer(serializers.Serializer):
    title = serializers.CharField()
    image = serializers.ImageField()
    corrected_x = serializers.DecimalField(max_digits=25, decimal_places=17)
    corrected_y = serializers.DecimalField(max_digits=25, decimal_places=17)
    note = serializers.CharField()
    flag = serializers.IntegerField()
    tags = serializers.CharField()