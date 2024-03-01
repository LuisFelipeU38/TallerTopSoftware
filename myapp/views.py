from django.shortcuts import get_object_or_404, render, redirect
from .models import Videojuego
from .forms import VideojuegoForm

def index(request):
    return render(request, 'index.html')

def opcion_uno(request):
    if request.method == 'POST':
        form = VideojuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('elemento_creado')
    else:
        form = VideojuegoForm()
    return render(request, 'opcion_uno.html', {'form': form})


def opcion_dos(request):
    videojuegos = Videojuego.objects.all()
    if not videojuegos:
        mensaje = "No existen videojuegos."
    else:
        mensaje = None
    return render(request, 'opcion_dos.html', {'videojuegos': videojuegos, 'mensaje': mensaje})

def elemento_creado(request):
    return render(request, 'elemento_creado.html')

def detalle_videojuego(request, videojuego_id):
    videojuego = get_object_or_404(Videojuego, pk=videojuego_id)
    return render(request, 'detalle_videojuego.html', {'videojuego': videojuego})

def borrar_videojuego(request, videojuego_id):
    videojuego = Videojuego.objects.get(pk=videojuego_id)
    videojuego.delete()
    return redirect('opcion_dos')