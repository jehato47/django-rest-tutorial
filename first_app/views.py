from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Country
from .serializers import CountrySerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.


class CountryView(APIView):
    def get(self, request):
        obj = Country.objects.all()
        serializer = CountrySerializer(obj, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = CountrySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)


class CountryDetailView(APIView):
    def get_object(self, pk):
        try:
            country = Country.objects.get(pk=pk)
            return country
        except Country.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        country = self.get_object(pk)
        serializer = CountrySerializer(country)
        return Response(serializer.data)

    def put(self, request, pk):
        country = self.get_object(pk)
        serializer = CountrySerializer(country, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        country = self.get_object(pk)

        country.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
