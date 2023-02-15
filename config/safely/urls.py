from django.urls import path
from safely.views import *
from config.urls import *

urlpatterns = [
    path('', conversion, name='pagCon'),
    path('conversionB/', conversionB, name='pagConB'),
    path('entrega/', entregaCarnada, name='entr'),
    path('entregaB/', entregaCarnadaB, name='entrB')
]