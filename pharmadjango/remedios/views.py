from django.shortcuts import render
from django.http import HttpResponse
from .models import Remedio
from django.template import loader

def lista_medicamentos(request):
    """lista todos os medicamentos cadastrados

        Args:
            request (request): requisição do usuário

    """
    remedios = Remedio.objects.all()
    context = {'remedios': remedios}
    return render(request, 'remedios/index.html', context)