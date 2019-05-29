from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer

class PersonListAPIView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class CreatePersonAPIView(CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class DeletePersonAPIView(APIView):
    def get(self, request, id):
        try:
            person = Person.objects.get(pk=id)
            person.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

class UpdatePersonAPIView(APIView):
    def patch(self, request, id):
        try:
            person = Person.objects.get(pk=id)
            serializer = PersonSerializer(person, data=request.data, partial=True) # set partial=True to update a data partially
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)