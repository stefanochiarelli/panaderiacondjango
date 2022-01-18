from django import forms


class CompraFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    producto = forms.CharField()
    tipo = forms.ChoiceField(choices=[('par', 'Pan'), ('torta', 'Torta'), ('facturas', 'Facturas')])
    cantidad= forms.IntegerField()
    calle = forms.CharField()
    altura = forms.CharField()
    localidad = forms.CharField()  