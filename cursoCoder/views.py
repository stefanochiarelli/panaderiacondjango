from django.http import HttpResponse
from django.shortcuts import render

def saluda(req):
    return HttpResponse('Hola como va, estoy creando mi primer controlador')


def probandoTemplate(self):
    return render(self, 'C:/Users/Stefano/Desktop/Coding Projects/python/Django Project/cursoCoder/cursoCoder/templates/template1.html')