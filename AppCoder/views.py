from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

def curso(request):

    curso = Curso(nombre="Django", comision="9393")
    curso.save()
    texto = f"Curso creado: {curso.nombre}, comision: {curso.comision}"
    return HttpResponse(texto)

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

