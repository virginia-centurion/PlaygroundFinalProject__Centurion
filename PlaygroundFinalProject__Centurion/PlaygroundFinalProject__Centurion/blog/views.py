from django.shortcuts import get_object_or_404
from .models import Post
from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib import messages

# Create your views here.

def inicio(request): # Lógica para la vista de inicio
    return render(request, 'blog/inicio.html')

def acerca_de(request):
    return render(request, 'blog/acerca_de.html')

def blog_lista(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog_lista.html', {'posts': posts})

def blog_detalle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/blog_detalle.html', {'post': post})

#@login_required
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, '¡El posteo ha sido creado con éxito!')
            return redirect('crear_post')  # Redirige al formulario de creación de posteos
    else:
        form = PostForm()
    return render(request, 'blog/crear_post.html', {'form': form})  # Asegúrate de pasar el formulario como contexto aquí


