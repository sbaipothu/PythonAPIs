from django.shortcuts import render

# Create your views here.
from .models import Employees, Course, Person
from .serializers import EmployeeSerializer, CourseSerializer, PersonSerializer
from rest_framework import viewsets


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employees.objects.all()


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
