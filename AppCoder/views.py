from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

# Create your views here.
def curso(self):
    curso = Curso(nombre='Desarrollo Web', camada='19881')
    curso.save()

    documentodeTexto = f'---->Curso: {curso.nombre} Camada: {curso.camada}'

    return HttpResponse(documentodeTexto)

def inicio(request):
    return render(request, 'inicio.html')

def cursos(request):
    return render(request, 'cursos.html')

def profesores(request):
    return HttpResponse('Vista Profesores')

def estudiantes(request):
    return HttpResponse('Vista Estudiantes')

def entregables(request):
    return HttpResponse('Vista Entregables')

