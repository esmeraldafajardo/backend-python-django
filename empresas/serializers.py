from rest_framework import serializers
from .models import Empresa

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'
        # fields = ['id', 'nit', 'nombre', 'direccion', 'telefono'] 

