from django.shortcuts import render
from django.views.generic import TemplateView, ListView,UpdateView,DeleteView,CreateView
from .models import Prueba #importa el modelo que hemos creado llamado "Prueba"
from django.views.generic import TemplateView
from django.urls import reverse_lazy                             # para redireccionar después de actualizar

# Create your views here.


class ListarPruebaListView(ListView):
    template_name = "mostrar_datos.html"
    model = Prueba
    context_object_name = 'lista'


# Vista para actualizar un registro existente
class EditarUpdateView(UpdateView):                              # vista que permite editar registros existentes
    model = Prueba                                               # modelo que se va a editar
    template_name = "editar_datos.html"                         # HTML que muestra el formulario para editar
    fields = ['titulo', 'subtitulo', 'cantidad']                # campos del modelo que se podrán modificar
    success_url = reverse_lazy('lista')                          # URL a donde redirige después de guardar cambios


class EliminarDeleteView(DeleteView):
    model = Prueba
    template_name = "eliminar_confirmacion.html"
    success_url = reverse_lazy('lista')

class CrearCreateView(CreateView):
    model = Prueba
    template_name = 'crear_datos.html'
    fields = ['titulo', 'subtitulo', 'cantidad']
    success_url = reverse_lazy('lista')