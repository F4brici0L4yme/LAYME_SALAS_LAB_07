from django.shortcuts import render
from .models import DestinosTuristicos
# Create your views here.


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

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroUsuarioForm
from django.contrib import messages

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado exitosamente.')
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro.html', {'form': form})

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
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def listar_destinos(request):
    return render(request, 'travelApp/listar_destinos.html')

def agregar_destino(request):
    return render(request, 'travelApp/agregar_destino.html')

def editar_destino(request):
    return render(request, 'travelApp/editar_destino.html')

def eliminar_destino(request):
    return render(request, 'travelApp/eliminar_destino.html')