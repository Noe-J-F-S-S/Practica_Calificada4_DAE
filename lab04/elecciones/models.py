from django.db import models



class Region(models.Model):
    region_texto = models.CharField(max_length=200)
    nombre_region = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Candidato(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    candidato_texto = models.CharField(max_length=200)
    ocupacion = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
    edad = models.CharField(max_length=200)
    partido = models.CharField(max_length=200)