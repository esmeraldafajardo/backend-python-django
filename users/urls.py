from django.urls import path
from .views import LoginView
from .views import crear_usuario,listar_usuarios,eliminar_usuario

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('crear/', crear_usuario),
    path('usuarios/', listar_usuarios),
    path('usuarios/<str:username>/', eliminar_usuario),
]
