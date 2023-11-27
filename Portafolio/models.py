from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()