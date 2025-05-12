# Create your views here.
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

import openai
from rest_framework import status



class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


@api_view(['POST'])
def generar_descripcion_automatica(request):
    nombre = request.data.get('nombre', '')
    caracteristicas = request.data.get('caracteristicas', '')
    
    if not nombre or not caracteristicas:
        return Response({'error': 'Faltan datos'}, status=400)

    # Simulamos IA
    descripcion = f"El producto '{nombre}' destaca por sus características: {caracteristicas}. Ideal para múltiples usos."

    return Response({'descripcion_generada': descripcion})



# @api_view(['POST'])
# def generar_descripcion_automatica(request):
#     nombre = request.data.get('nombre')
#     caracteristicas = request.data.get('caracteristicas')

#     if not nombre or not caracteristicas:
#         return Response({'error': 'Faltan datos'}, status=status.HTTP_400_BAD_REQUEST)

#     prompt = f"Genera una descripción atractiva para un producto llamado '{nombre}' con las siguientes características: {caracteristicas}"

#     try:
#         respuesta = openai.Completion.create(
#             engine="text-davinci-003",  # Puedes usar gpt-3.5-turbo si tienes acceso
#             prompt=prompt,
#             max_tokens=100,
#             temperature=0.7
#         )
#         descripcion = respuesta.choices[0].text.strip()
#         return Response({'descripcion_generada': descripcion})
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
