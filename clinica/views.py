from django.shortcuts import render
from rest_framework import viewsets
from .models import FichaClinica, Recordatorio
from .serializers import FichaClinicaSerializer, RecordatorioSerializer

class FichaClinicaViewSet(viewsets.ModelViewSet):
    queryset = FichaClinica.objects.all()
    serializer_class = FichaClinicaSerializer

class RecordatorioViewSet(viewsets.ModelViewSet):
    queryset = Recordatorio.objects.all()
    serializer_class = RecordatorioSerializer