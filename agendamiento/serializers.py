from rest_framework import serializers
from .models import Profesional, CitaMedica

class ProfesionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesional
        fields = '__all__'

class CitaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitaMedica
        fields = '__all__'