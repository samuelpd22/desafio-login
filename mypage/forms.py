from django import forms
from django.core.exceptions import ValidationError
import re
from .models import Usuario

class RegistroForm(forms.ModelForm):
    confirmar_senha = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirmar Senha"
    )

    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'pattern': '[A-Za-zÀ-ÖØ-öø-ÿ\s]+', 'title': 'O nome deve conter apenas letras.'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'senha': 'Senha'
        }

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if not re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$', nome):
            raise ValidationError("O nome deve conter apenas letras.")
        return nome

    def clean_email(self):
        email = self.cleaned_data['email']
        if Usuario.objects.filter(email=email).exists():
            raise ValidationError("E-mail já cadastrado!")
        return email

    def clean_senha(self):
        senha = self.cleaned_data['senha']
        if len(senha) < 8:
            raise ValidationError("A senha deve ter pelo menos 8 caracteres.")
        if not re.search(r'[A-Z]', senha):
            raise ValidationError("A senha deve conter pelo menos uma letra maiúscula.")
        if not re.search(r'\d', senha):
            raise ValidationError("A senha deve conter pelo menos um número.")
        if not re.search(r'[\W_]', senha):
            raise ValidationError("A senha deve conter pelo menos um caractere especial (!@#$%^&*).")
        return senha

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        confirmar_senha = cleaned_data.get('confirmar_senha')

        if senha and confirmar_senha and senha != confirmar_senha:
            raise ValidationError({'confirmar_senha': "As senhas não coincidem!"})

        return cleaned_data
