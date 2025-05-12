from rest_framework import serializers
from .models import Inventario

class InventarioSerializer(serializers.ModelSerializer):
    empresa_nombre = serializers.CharField(source='empresa.nombre', read_only=True)
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)

    class Meta:
        model = Inventario
        fields = ['id', 'empresa', 'producto', 'cantidad', 'empresa_nombre', 'producto_nombre']
