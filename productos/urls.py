from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, generar_descripcion_automatica

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('generar-descripcion/', generar_descripcion_automatica),

]
