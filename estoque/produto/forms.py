from django.forms import ModelForm
from django import forms
from .models import Produtos

class ProdutoForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['produto', 'cor', 'descricao']
        widgets = { 
            'produto': forms.TextInput(attrs={ 
            'class': 'input', 
            'placeholder': 'Nome do produto', 
      }), 
           'descricao': forms.Textarea(attrs={ 
            'class': 'textarea', 
            'placeholder': 'Escreva a descrição...', 
      }), 
      }