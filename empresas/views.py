from rest_framework import viewsets
from rest_framework.permissions import BasePermission, SAFE_METHODS,IsAuthenticatedOrReadOnly
from .models import Empresa
from .serializers import EmpresaSerializer

# Permiso personalizado
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Solo permite métodos seguros (GET, HEAD, OPTIONS) a externos
        if request.method in SAFE_METHODS:
            return True
        # Solo usuarios autenticados con rol admin pueden POST, PUT, DELETE
        return request.user.is_authenticated and getattr(request.user, 'rol', '') == 'admin'

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]