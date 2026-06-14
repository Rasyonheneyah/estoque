from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'index.html', {'mensagem': 'Olá! Seja bem-vindo à aplicação web do estoque!'}    )


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    template_name = 'register.html'
    context = {
        'form': form
    }
    return render(request, template_name, context)
