# from django.shortcuts import render
# from django.views.generic import TemplateView

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from photobase.models import SiteDoc, Image
from photobase.serializers import (
    SiteDocSerializer,
    ImageSerializer
)

# Create your views here.

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
        return Image.objects.all()

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
