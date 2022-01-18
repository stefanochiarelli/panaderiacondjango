from coderApp.forms import CompraFormulario
from django.shortcuts import render
from coderApp.models import Producto, datosPersona, Direccion

# Create your views here.


def inicio(self):
    return render(self, 'inicio.html')

def sucursales(self):
    return render(self, 'nuestras.html')


def contacto(request):

    if request.method == 'POST':
        miForm = CompraFormulario(request.POST)
        print(miForm)

        if miForm.is_valid():

            data = miForm.cleaned_data

            

            producto = Producto(producto=data['producto'], tipo=data['tipo'], cantidad=data['cantidad'])
            datosPers = datosPersona(nombre=data['nombre'], apellido=data['apellido'], email=data['email'])
            direc = Direccion(calle=data['calle'], altura=data['altura'], localidad=data['localidad'])

            producto.save()
            datosPers.save()
            direc.save()

            return render(request, 'thankyoupage.html')



    else:    
        miForm = CompraFormulario()
    
    return render(request, 'contacto.html', {'compraForm': miForm})


def busquedaCompra(request):
    return render(request, 'busqueda.html')

def buscar(req):

    if req.GET['email']:
        email = req.GET['email']
        emailFiltered = datosPersona.objects.filter(email__icontains=email)
        # print(emailFiltered)
        return render(req, 'busquedaCompleta.html', {'datoEmail':emailFiltered})

