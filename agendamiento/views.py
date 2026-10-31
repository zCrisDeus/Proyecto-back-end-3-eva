from django.shortcuts import render
from rest_framework import viewsets
from .models import Profesional, CitaMedica
from .serializers import ProfesionalSerializer, CitaMedicaSerializer

class ProfesionalViewSet(viewsets.ModelViewSet):
    queryset = Profesional.objects.all()
    serializer_class = ProfesionalSerializer

class CitaMedicaViewSet(viewsets.ModelViewSet):
    queryset = CitaMedica.objects.all()
    serializer_class = CitaMedicaSerializer