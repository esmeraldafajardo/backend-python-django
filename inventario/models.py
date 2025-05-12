# Create your models here.
from django.db import models
from productos.models import Producto
from empresas.models import Empresa

class Inventario(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.producto.nombre} - {self.empresa.nombre}"
