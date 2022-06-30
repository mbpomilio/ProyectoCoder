from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

def curso(request):

    curso = Curso(nombre="Django", comision="9393")
    curso.save()
    texto = f"Curso creado: {curso.nombre}, comision: {curso.comision}"
    return HttpResponse(texto)