from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto

        fields = [
            'nombre',
            'precio',
            'descripcion'
        ]

        widgets = {

            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del producto'
            }),

            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Precio del producto',
                'step': '0.01',
                'min': '0.01'
            }),

            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción del producto',
                'rows': 3
            }),

        }