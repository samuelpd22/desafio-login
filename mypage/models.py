import re
from django.core.exceptions import ValidationError
from django.db import models

def validar_nome(value):
    if not re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$', value):
        raise ValidationError('O nome deve conter apenas letras.')

def validar_senha(value):
    if len(value) < 8 or not re.search(r'[A-Z]', value) or not re.search(r'\d', value) or not re.search(r'\W', value):
        raise ValidationError('A senha deve ter pelo menos 8 caracteres, 1 letra maiúscula, 1 número e 1 caractere especial.')

class Usuario(models.Model):
    nome = models.CharField(max_length=100, validators=[validar_nome])
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255, validators=[validar_senha])

    def __str__(self):
        return self.nome
