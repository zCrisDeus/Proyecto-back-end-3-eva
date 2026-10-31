from django.db import models
from pacientes.models import Mascota

class Profesional(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Profesional"
        verbose_name_plural = "Profesionales"

    def __str__(self):
        return f"Dr/a. {self.nombre} {self.apellidos} - {self.especialidad}"

class CitaMedica(models.Model):
    ESTADOS_CHOICES = [
        ('PROGRAMADA', 'Programada'),
        ('COMPLETADA', 'Completada'),
        ('CANCELADA', 'Cancelada'),
    ]

    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='citas')
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, related_name='citas')
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS_CHOICES, default='PROGRAMADA')

    class Meta:
        verbose_name = "Cita Médica"
        verbose_name_plural = "Citas Médicas"
        # Esta es la regla de negocio que evita el solapamiento de citas
        unique_together = ('profesional', 'fecha', 'hora')

    def __str__(self):
        return f"{self.fecha} {self.hora} | {self.mascota.nombre} con {self.profesional.nombre}"