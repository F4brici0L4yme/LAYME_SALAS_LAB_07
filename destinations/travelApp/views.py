from .models import DestinosTuristicos
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroUsuarioForm  # Este debe ser un formulario que extiende UserCreationForm
from django.contrib import messages

from .models import DestinosTuristicos
from django.contrib.auth.decorators import login_required


@login_required
def listar_destinos(request):
    destinos = DestinosTuristicos.objects.all()
    return render(request, '../templates/listar_destinos.html', {'destinos': destinos})


@login_required
def agregar_destino(request):
    if request.method == 'POST':
        nombre = request.POST['nombreCiudad']
        descripcion = request.POST['descripcionCiudad']
        imagen = request.FILES['imagenCiudad']
        precio = request.POST['precioTour']
        oferta = 'ofertaTour' in request.POST

        destino = DestinosTuristicos(
            nombreCiudad=nombre,
            descripcionCiudad=descripcion,
            imagenCiudad=imagen,
            precioTour=precio,
            ofertaTour=oferta
        )
        destino.save()
        return redirect('/listar')

    return render(request, '../templates/agregar_destino.html')

@login_required
def editar_destino(request, pk):
    destino = DestinosTuristicos.objects.get(id=pk)
    if request.method == 'POST':
        destino.nombreCiudad = request.POST['nombreCiudad']
        destino.descripcionCiudad = request.POST['descripcionCiudad']
        if 'imagenCiudad' in request.FILES:
            destino.imagenCiudad = request.FILES['imagenCiudad']
        destino.precioTour = request.POST['precioTour']
        destino.ofertaTour = 'ofertaTour' in request.POST
        destino.save()
        return redirect('listar_destinos')  # Cambia 'editar' por la vista correcta

    return render(request, '../templates/editar_destino.html', {'destino': destino})


from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import DestinosTuristicos

@login_required
def eliminar_destino(request, pk):
    destino = get_object_or_404(DestinosTuristicos, pk=pk)
    destino.delete()
    return redirect('listar_destinos')


def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado exitosamente.')
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, '../templates/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('listar_destinos')
        else:
            messages.error(request, 'Credenciales incorrectas.')
    return render(request, '../templates/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

def index(request):

    dest1 = DestinosTuristicos()
    dest1.name = 'Mumbai'
    dest1.desc = 'The City That Never Sleeps'
    dest1.img = 'destination_1.jpg'
    dest1.price = 700

    dest2 = DestinosTuristicos()
    dest2.name = 'Hyderabad'
    dest2.desc = 'First Biryani, Then Sherwani'
    dest2.img = 'destination_2.jpg'
    dest2.price = 650

    dest3 = DestinosTuristicos()
    dest3.name = 'Bengaluru'
    dest3.desc = 'Beautiful City'
    dest3.img = 'destination_3.jpg'
    dest3.price = 750

    dests = [dest1, dest2, dest3]

    return render(request, "index.html", {'dests': dests})
