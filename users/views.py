# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            return Response({
                'message': f'Bienvenido {user.username}',
                'rol': user.rol,
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
# @permission_classes([IsAdminUser])  # Solo admin puede crear usuarios
def crear_usuario(request):
    username = request.data.get('username')
    password = request.data.get('password')
    rol = request.data.get('rol')

    if not all([username, password, rol]):
        return Response({'error': 'Faltan campos'}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'El usuario ya existe'}, status=400)

    user = User.objects.create_user(username=username, password=password, rol=rol)
    return Response({'message': 'Usuario creado correctamente'})

@api_view(['GET'])
# @permission_classes([IsAdminUser])
def listar_usuarios(request):
    data = list(User.objects.values('username', 'rol'))
    return Response(data)


@api_view(['DELETE'])
# @permission_classes([IsAdminUser])
def eliminar_usuario(request, username):
    try:
        user = User.objects.get(username=username)
        user.delete()
        return Response({'message': f'Usuario {username} eliminado'}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)