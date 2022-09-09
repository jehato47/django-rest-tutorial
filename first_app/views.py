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
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.decorators import authentication_classes, permission_classes
from django_course_youtube.permission import HasAInUsername


# Create your views here.

class GenericApiView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
    mixins.UpdateModelMixin, mixins.DestroyModelMixin,
):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, HasAInUsername]

    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    lookup_field = "pk"

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request)

        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


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


@api_view(["GET", "POST"])
def login(request):
    data = request.data

    auth = authenticate(username=data["username"], password=data["password"])

    if auth:
        token = Token.objects.filter(user=auth).first()

        if not token:
            token = Token.objects.create(user=auth)

        return Response({"success": True, "token": token.key})

    return Response({"success": False, "message": "Username or Password is incorrect"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(["DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    Token.objects.filter(user=request.user).delete()
    return Response(True)
