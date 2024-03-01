from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('opcion-uno/', views.opcion_uno, name='opcion_uno'),  # Define la URL con nombre 'opcion_uno'
    path('opcion-dos/', views.opcion_dos, name='opcion_dos'),  # Define la URL con nombre 'opcion_dos'
    path('elemento-creado/', views.elemento_creado, name='elemento_creado'),
    path('detalle-videojuego/<int:videojuego_id>/', views.detalle_videojuego, name='detalle_videojuego'),
    path('borrar-videojuego/<int:videojuego_id>/', views.borrar_videojuego, name='borrar_videojuego'),
]
