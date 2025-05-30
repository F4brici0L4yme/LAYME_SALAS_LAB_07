from django import forms
from django.contrib.auth.models import User  # 👈 Importación necesaria

class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput(),
        }
