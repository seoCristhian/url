from django.shortcuts import render

# Create your views here.
def conversion(request):
    return render(request, 'paginaConversion.html')

def conversionB(request):
    return render(request, 'paginaConversionB.html')

def entregaCarnada(request):
    return render(request, 'entregaCarnada.html')

def entregaCarnadaB(request):
    return render(request, 'entregaCarnadaB.html')

