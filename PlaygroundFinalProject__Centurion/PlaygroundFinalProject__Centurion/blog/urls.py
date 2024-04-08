from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # La URL raíz redirige a la vista 'inicio'
    path('sobre/', views.acerca_de, name='acerca_de'),  # URL para la vista 'Acerca de mí'
    path('pages/', views.blog_lista, name='blog_lista'),  # URL para la vista de lista de blogs
    path('pages/<int:pk>/', views.blog_detalle, name='blog_detalle'),  # URL para la vista de detalle de un blog
    path('crear_post/', views.crear_post, name='crear_post'),  # URL para la vista de creación de un nuevo post
    
]
