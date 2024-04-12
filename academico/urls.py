
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarCursos/', views.registrarCursos),
    path('edicionCurso/<codigo>', views.edicionCurso),
    path('editarCursos/', views.editarCursos),
    path('eliminacionCurso/<codigo>', views.eliminacionCurso)
]
