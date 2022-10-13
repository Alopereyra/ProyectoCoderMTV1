from re import template
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.
from AppCoder.models import Profesor

from AppCoder.models import Familiares


def crear_familiar(request):
    template = loader.get_template("template1.html")
    
    pariente = Familiares(nombre="Eduardo, ", parentezco="Padre, ", edad="69, ", fecha_de_nacimiento="1953-02-06")
    pariente2 = Familiares(nombre="Mirta, ", parentezco="Madre, ", edad="67, ", fecha_de_nacimiento="1955-03-08")
    pariente3 = Familiares(nombre="Lorena, ", parentezco="Esposa, ", edad="36, ", fecha_de_nacimiento="1986-10-02")
    pariente4 = Familiares(nombre="Luciano, ", parentezco="Hermano, ", edad="26, ", fecha_de_nacimiento="1996-01-22")
    
    pariente.save()
    pariente2.save()
    pariente3.save()
    pariente4.save()
    
    
    dict_de_contexto = {
        "familia": pariente,
        "familia_2": pariente2, 
        "familia_3": pariente3,
        "familia_4": pariente4,
    }
    res = template.render(dict_de_contexto)
    return HttpResponse(res)

def crear_profesor(request):
    template = loader.get_template("template1.html")
    
    profe = Profesor(nombre="Ricardo", apellido="Ruben", email="ricky@ar", profesion="abogado")
    profe2 = Profesor(nombre="Manuel", apellido="Saenz", email="manu@ar", profesion="abogado")
    profe3 = Profesor(nombre="Ezequiel", apellido="Batera", email="eze@ar", profesion="contador")
    
    dict_de_contexto = {
        "profe_1": profe,
        "profe_2": profe2, 
        "profe_3": profe3,
    }
    res = template.render(dict_de_contexto)
    return HttpResponse(res)




