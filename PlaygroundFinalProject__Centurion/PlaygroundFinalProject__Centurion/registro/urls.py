# urls.py de la aplicación registro
from django.urls import path
from . import views

urlpatterns = [
    # Eliminar esta línea para evitar conflictos
    # path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    
    ]