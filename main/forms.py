from django.forms import *
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "quantity"]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control form-control-border', 'placeholder': 'Name'}),
            'price': NumberInput(attrs={'class': 'form-control form-control-border', 'placeholder': 'Price'} ),
            'quantity': NumberInput(attrs={'class': 'form-control form-control-border', 'placeholder': 'Quantity'}),
            'description': Textarea(attrs={'class': 'form-control form-control-border', 'placeholder': 'Description'}),
        }