from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import Template, Context
from .forms import ContactoForm


def home(request):
    plantillaExterna = open("c:/Portafolio/Portafolio/templates/home.html")
    template = Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto = Context()
    documento = template.render(contexto)
    return render(request, "home.html", {'form': ContactoForm()})

def createForm(request):
    data = {
        'form': ContactoForm()
    }
    return render(request, 'home.htm', data)
    