from django.shortcuts import render, redirect
from .models import Produtos
from .forms import ProdutoForm

from django.contrib.auth.decorators import login_required 


@login_required
def list_produto(request):
    produtos = Produtos.objects.all()
    template_name = 'list_produtos.html'
    context = {
        'produtos': produtos
    }
    return render(request, template_name, context)

@login_required
def new_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('produto:list_produto')
    else:
        template_name = 'form_produto.html'
        context = {
            'form': ProdutoForm(),
        }
        return render(request, template_name, context)

@login_required
def update_produto(request, pk):
    produto = Produtos.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produto:list_produto')
    else:
        template_name = 'form_produto.html'
        context = {
            'form': ProdutoForm(instance=produto)
        }
        return render(request, template_name, context)

@login_required
def delete_produto(request, pk):
    produto = Produtos.objects.get(pk=pk)
    produto.delete()
    return redirect('produto:list_produto')