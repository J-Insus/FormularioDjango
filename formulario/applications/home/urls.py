from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [

    path('mostrar_datos/', views.ListarPruebaListView.as_view() , name='lista'),
    path('editar/<int:pk>/', views.EditarUpdateView.as_view(), name='editar'),  # vista para editar, con ID dinámico
    path('eliminar/<int:pk>/', views.EliminarDeleteView.as_view(), name='eliminar'),
    path('crear/', views.CrearCreateView.as_view(), name='crear'),

]