from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Saidas
from .forms import SaidaForm
from django.contrib.auth.decorators import login_required 



@login_required
def list_saida(request):
    saidas = Saidas.objects.all()
    template_name = 'list_saida.html'
    context = {
        'saidas': saidas
    }
    return render(request, template_name, context)

@login_required
def new_saida(request):
    if request.method == 'POST':
        form = SaidaForm(request.POST)

        if form.is_valid():
            form.save(commit=False)
            if form.cleaned_data['quantidade'] <= form.cleaned_data['produto'].quantidade and form.cleaned_data['quantidade'] >= 1:
                
                form.cleaned_data['produto'].quantidade -= form.cleaned_data['quantidade']
                
                form.cleaned_data['produto'].save_base()
                form.save()

        return redirect('saida:list_saida')
    else:
        template_name = 'form_saida.html'
        context = {
            'form': SaidaForm() 
        }
        return render(request, template_name, context)


@login_required
def update_saida(request, pk):
    saida = Saidas.objects.get(pk=pk)

    if request.method == 'POST':
        form = SaidaForm(request.POST, instance=saida)
        quantidade = saida.quantidade

        if form.is_valid():
            form.save(commit = False)
            if form.cleaned_data['quantidade'] <= form.cleaned_data['produto'].quantidade + quantidade and form.cleaned_data['quantidade'] >= 1:

                form.cleaned_data['produto'].quantidade = (form.cleaned_data['produto'].quantidade - form.cleaned_data['quantidade']) + quantidade
                form.cleaned_data['produto'].save_base()
                form.save()

            return redirect('saida:list_saida')
    else:
        template_name = 'form_saida.html'
        context = {
            'form': SaidaForm(instance=saida),
            'pk': pk,

        }
        return render(request, template_name, context)

@login_required
def delete_saida(request, pk):
    saida = Saidas.objects.get(pk=pk)
    saida.produto.quantidade = saida.produto.quantidade + saida.quantidade
    saida.produto.save()
    saida.delete()
    return redirect('saida:list_saida')
    