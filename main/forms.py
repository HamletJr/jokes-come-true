from django.forms import *
from main.models import Product
from django.utils.html import strip_tags
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

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)