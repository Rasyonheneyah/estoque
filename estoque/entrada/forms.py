from django.forms import ModelForm, NumberInput, Select
from django import forms
from .models import Entradas

class EntradaForm(ModelForm):
    class Meta:
        model = Entradas
        fields = ['produto', 'quantidade', 'preco']
        widgets = {
            'preco': NumberInput(attrs={
                'class': 'input',
                'placeholder': 'Preço do Produto',
                'min': '0',
                'step': '0.01'
            }),
            
            'produto': forms.Select(attrs={
                'class': 'select',
                'style': 'width: 50%;'
            }),
            'quantidade': NumberInput(attrs={
                'class': 'input',
                'min': '0',
                'step': '1',
                'style':'width: 95%;',
            }),
            'disponivel': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }

        labels = { 
        'produto': 'Produto', 
        'descricao': 'Descrição', 
        'cor': 'Cor', 
        'preco': 'Preço (R$)', 
        'quantidade': 'Quantidade', 
        }