from django.shortcuts import render
from django.template import Template, Context
from .forms import ContactoForm
from .models import Contacto
from decouple import config

def home(request):
    plantillaExterna = open(config('RUTA_PORTAFOLIO'))
    template = Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto = Context()
    documento = template.render(contexto)
    formulario(request)
    return render(request, "home.html", {'form': ContactoForm()})


def formulario(request):
    form = ContactoForm()

    if request.method == "POST":
        form = ContactoForm(request.POST)

        if form.is_valid():
             
            contacto = Contacto()
            contacto.nombre = form.cleaned_data['nombre'],
            contacto.telefono = form.cleaned_data['telefono'],
            contacto.email = form.cleaned_data['email']
            
            contacto.save()

        
    
    