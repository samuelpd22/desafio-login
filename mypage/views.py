from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroForm
from .models import Usuario
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.senha = make_password(form.cleaned_data['senha']) 
            usuario.save()
            messages.success(request, "Cadastro realizado com sucesso! Faça login.")
            return redirect('registro')
        else:
            messages.error(request, "Corrija os erros abaixo.")
    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        try:
            usuario = Usuario.objects.get(email=email)
            if check_password(senha, usuario.senha): 
                return render(request, 'dashboard.html', {'usuario': usuario})
            else:
                return render(request, 'login.html', {'erro': 'Senha incorreta!'})
        except Usuario.DoesNotExist:
            return render(request, 'login.html', {'erro': 'Usuário não encontrado!'})

    return render(request, 'login.html')