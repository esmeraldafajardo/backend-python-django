from rest_framework.routers import DefaultRouter
from .views import InventarioViewSet, generar_pdf, enviar_pdf_por_correo
from django.urls import path

router = DefaultRouter()
router.register(r'', InventarioViewSet)  # <- ✅ sin 'inventario' repetido

urlpatterns = [
    path('pdf/', generar_pdf, name='generar_pdf'),
    path('enviar/', enviar_pdf_por_correo, name='enviar_pdf'),
]

urlpatterns += router.urls
