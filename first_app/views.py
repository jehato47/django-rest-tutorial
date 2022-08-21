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
        # data = JSONParser().parse(request)
        serializer = CountrySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)


class CountryDetailView(APIView):
    def get_object(self, id):
        try:
            country = Country.objects.get(id=id)
            return country
        except Country.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        country = self.get_object(pk)
        serializer = CountrySerializer(country)
        return Response(serializer.data)

    def put(self, request, pk):
        country = self.get_object(pk)
        # data = JSONParser().parse(request)
        serializer = CountrySerializer(country, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        country = self.get_object(pk)
        country.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def country_list(request):
    if request.method == "GET":
        obj = Country.objects.all()
        serializer = CountrySerializer(obj, many=True)

        return Response(serializer.data)

    elif request.method == "POST":
        # data = JSONParser().parse(request)
        serializer = CountrySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    return HttpResponse(status=400)


@api_view(["GET", "PUT", "DELETE"])
def country_detail(request, pk):
    try:
        country = Country.objects.get(pk=pk)
    except Country.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CountrySerializer(country)
        return Response(serializer.data)

    elif request.method == "PUT":
        # data = JSONParser().parse(request)
        serializer = CountrySerializer(country, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    elif request.method == "DELETE":
        country.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
