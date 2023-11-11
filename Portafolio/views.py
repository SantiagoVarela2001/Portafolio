from django.http import HttpResponse
from django.template import Template, Context


def home(request):
    plantillaExterna = open("c:/Portafolio/Portafolio/plantillas/home.HTML")
    template = Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)