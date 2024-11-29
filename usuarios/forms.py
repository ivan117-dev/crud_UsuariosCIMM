from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioForm(forms.ModelForm):
    class Meta:
        model= Usuario
        fields = ['nombre','apellidos','fecha_nac','usuario','password','foto']
        foto = forms.ImageField(required=False)

class registroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']