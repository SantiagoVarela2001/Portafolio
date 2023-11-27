from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import Template, Context
from .forms import ContactoForm
from .models import Contacto


def home(request):
    plantillaExterna = open("c:/Portafolio/Portafolio/templates/home.html")
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
            contacto.telefono=form.cleaned_data['telefono'],
            contacto.email=form.cleaned_data['email']
            
            contacto.save()

        
    
    