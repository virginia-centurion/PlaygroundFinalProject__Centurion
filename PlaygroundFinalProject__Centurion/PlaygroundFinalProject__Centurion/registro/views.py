# views.py de la aplicación registro


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')  # Redirige a la página de inicio
        else:
            # Mensaje de error si las credenciales son inválidas
            return render(request, 'registro/login.html', {'error_message': 'Nombre de usuario o contraseña incorrectos.'})
    else:
        return render(request, 'registro/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige a la página de login después del logout

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Usuario registrado exitosamente!')
            return redirect('login')  # Redirige al inicio de sesión después del registro
    else:
        form = RegistroForm()
    return render(request, 'registro/registro.html', {'form': form})

@login_required
def view_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    elif request.method == 'DELETE':
        profile.delete()
        # Redireccionar a una página diferente o cerrar sesión, según tus necesidades
        return redirect('logout')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'registro/profile.html', {'profile': profile, 'form': form})

@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'registro/edit_profile.html', {'form': form})

