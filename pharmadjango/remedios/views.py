from django.shortcuts import render
from django.http import HttpResponse
from .models import Remedio
from django.template import loader

def lista_medicamentos(request):
    template = loader.get_template("remedios/index.html")
    return HttpResponse(template.render())

# Create your views here.
