# from django.shortcuts import render
# from django.views.generic import TemplateView

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from photobase.models import Location, Coords, SitePlan, SiteDoc, Image
from photobase.serializers import (
    LocationSerializer, 
    CoordsSerializer, 
    SitePlanSerializer, 
    SiteDocSerializer,
    ImageSerializer
)

# syntatic sugars
GET = 'GET'
POST = 'POST'

# Create your views here.

class LocationView(APIView):

    def get_queryset(self):
        return Location.objects.all()

    def get(self, request, format=None):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)