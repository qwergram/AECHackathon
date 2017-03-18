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
        locations = self.get_queryset()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class CoordsView(APIView):

    def get_queryset(self):
        return Coords.objects.all()

    def get(self, request, format=None):
        coords = self.get_queryset()
        serializer = CoordsSerializer(coords, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CoordsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class SitePlanView(APIView):
    
    def get_queryset(self):
        return SitePlan.objects.all()

    def get(self, request, format=None):
        siteplans = self.get_queryset()
        serializer = SitePlanSerializer(siteplans, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SitePlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class SiteDocView(APIView):
    
    def get_queryset(self):
        return SiteDoc.objects.all()

    def get(self, request, format=None):
        sitedocs = self.get_queryset()
        serializer = SiteDocSerializer(sitedocs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SiteDocSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class ImageView(APIView):
    
    def get_queryset(self):
        return Images.objects.all()

    def get(self, request, format=None):
        sitedocs = self.get_queryset()
        serializer = ImageSerializer(sitedocs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
