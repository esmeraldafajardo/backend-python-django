from django.shortcuts import render

def presentacion_tecnica(request):
    return render(request, 'presentacion.html')
