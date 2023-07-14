from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso
from AppCoder.forms import CursoFormulario



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
    return render(request, 'profesores.html')

def estudiantes(request):
    return render(request, 'estudiantes.html')

def entregables(request):
    return render(request, 'entregables.html')

def cursoFormulario(request):
    if request.method == "POST":

        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

        curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])
        curso.save()
        return render(request, 'inicio.html')
    
    else:
        miFormulario = CursoFormulario()


    return render(request, 'cursoFormulario.html', {"miFormulario": miFormulario})





