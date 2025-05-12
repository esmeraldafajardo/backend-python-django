# Create your views here.
from django.http import FileResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from .models import Inventario
from django.core.mail import EmailMessage
from rest_framework import viewsets
from .serializers import InventarioSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]


def generar_pdf(request):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    inventario = Inventario.objects.all()
    y = 800

    for item in inventario:
        texto = f"Empresa: {item.empresa.nombre} | Producto: {item.producto.nombre} | Cantidad: {item.cantidad}"
        p.drawString(100, y, texto)
        y -= 20

    p.showPage()
    p.save()
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename='inventario.pdf')



def enviar_pdf_por_correo(request):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    inventario = Inventario.objects.all()
    y = 800
    for item in inventario:
        p.drawString(100, y, f"{item.empresa.nombre} - {item.producto.nombre} ({item.cantidad})")
        y -= 20
    p.showPage()
    p.save()
    buffer.seek(0)

    email = EmailMessage(
        'Inventario PDF',
        'Adjunto encontrarás el inventario.',
        'tusistema@correo.com',
        ['destino@correo.com'],
    )
    email.attach('inventario.pdf', buffer.read(), 'application/pdf')
    email.send()

    return FileResponse(BytesIO(b"Correo enviado correctamente"), content_type='text/plain')
