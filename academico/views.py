from django.shortcuts import render, redirect
from .models import Curso
# Create your views here.

def home (request):
    cursosListado = Curso.objects.all()
    return render(request, 'gestiosCursos.html', {"cursos": cursosListado})


def registrarCursos(request):
    codigo = request.POST['txtcodigo']
    nombre = request.POST['txtnombre']
    creditos = request.POST['numcreditos']
    
    curso = Curso.objects.create(
        codigo=codigo, nombre=nombre, creditos=creditos)

    return redirect('/')


def eliminacionCurso(request, codigo):
    curso=Curso.objects.get(codigo=codigo) 
    curso.delete()   
    return redirect('/')


def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, 'edicionCurso.html',{"curso":curso})
    

def editarCursos(request):
    codigo = request.POST['txtcodigo']
    nombre = request.POST['txtnombre']
    creditos = request.POST['numcreditos']
    curso = Curso.objects.get(codigo=codigo)

    curso.nombre = nombre
    curso.creditos= creditos
    curso.save()
    return redirect('/')
