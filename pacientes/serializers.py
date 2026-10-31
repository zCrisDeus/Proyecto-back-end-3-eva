from rest_framework import serializers
from .models import Tutor, Mascota

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'

class TutorSerializer(serializers.ModelSerializer):
    # Relación anidada para visualizar las mascotas directamente al consultar al tutor
    mascotas = MascotaSerializer(many=True, read_only=True)

    class Meta:
        model = Tutor
        fields = '__all__'