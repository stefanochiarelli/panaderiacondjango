from django.urls import path
from coderApp.views import inicio, sucursales, contacto, busquedaCompra, buscar



urlpatterns = [
    path('', inicio, name='inicio'),
    path('nuestras/', sucursales, name='sucus'),
    path('contacto/', contacto, name='contacto'),
    path('busqueda/', busquedaCompra, name='busqueda'),
    path('buscar/', buscar, name='buscar'),


]
