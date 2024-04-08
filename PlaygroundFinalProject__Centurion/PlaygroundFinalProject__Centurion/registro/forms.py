from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Profile

class RegistroForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text=_('Requerido. Proporciona una dirección de correo electrónico válida.'), label=_('Correo electrónico'))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
        labels = {
            'username': _('Usuario'),
            'password1': _('Contraseña'),
            'password2': _('Confirmar contraseña'),
        }
        help_texts = {
            'password1': _('Tu contraseña no puede ser demasiado similar a tu otra información personal.'),
            'password2': _('Debes ingresar la misma contraseña que antes, para verificación.'),
        }

class ProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True, label=_('Nombre de usuario'))
    email = forms.EmailField(max_length=254, required=True, label=_('Correo electrónico'))
    description = forms.CharField(max_length=255, required=True, label=_('Descripción'))
    website = forms.URLField(max_length=200, required=False, label=_('Link a la página web'))
    password = forms.CharField(widget=forms.PasswordInput, required=True, label=_('Contraseña'))

    class Meta:
        model = Profile
        fields = ['image', 'username', 'email', 'description', 'website', 'password']

