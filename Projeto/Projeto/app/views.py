from django.shortcuts import render
from . models import *

def consulta(request):
    consultas = {
        'consultas' :Livro.objects.all()
    }

    return render(request, 'consulta/consulta.html',consultas)
# Create your views here.
