"""
Models
"""
from django.db import models

class Ciudad(models.Model):
    """
    Ciudad
    """
    id = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    poblacion = models.PositiveIntegerField()
    latitud = models.FloatField()
    longitud = models.FloatField()

    def __str__(self):
        return f"{self.nombre}"

class Pronostico(models.Model):
    """
    Pronostico
    """
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    fecha_hora_txt = models.DateTimeField()
    dia_text = models.CharField(max_length=50)
    temperatura = models.FloatField()
    temp_min = models.FloatField()
    temp_max = models.FloatField()
    humedad = models.PositiveIntegerField()
    clima = models.CharField(max_length=50)
    viento_velocidad = models.FloatField()
    viento_direccion = models.PositiveIntegerField()
    visibilidad = models.PositiveIntegerField()
    probabilidad_precipitacion = models.FloatField()
    lluvia_volumen_1h = models.FloatField()

    def __str__(self):
        return f"{self.ciudad} - {self.fecha_hora_txt}"
