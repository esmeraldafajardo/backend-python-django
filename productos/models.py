# Create your models here.
from django.db import models
from empresas.models import Empresa

class Producto(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    caracteristicas = models.TextField()
    precio_usd = models.DecimalField(max_digits=10, decimal_places=2)
    precio_gtq = models.DecimalField(max_digits=10, decimal_places=2)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre
