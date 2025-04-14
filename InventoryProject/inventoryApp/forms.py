from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_id': "Product ID",
            'name': "Product Name",
            'sku': "Product SKU",
            'price': "Product Price",
            'quantity': "Product Quantity",
            'supplier': "Product Supplier",
        }
        widgets = {
            'product_id': forms.NumberInput(attrs={'placeholder':'e.g. 1','class':'form-control'}),
            'name': forms.TextInput(attrs={'placeholder':'e.g. Beans','class':'form-control'}),
            'sku': forms.TextInput(attrs={'placeholder':'e.g. s12345','class':'form-control'}),
            'price': forms.NumberInput(attrs={'placeholder':'e.g. 100.00','class':'form-control'}),
            'quantity': forms.NumberInput(attrs={'placeholder':'e.g. 10','class':'form-control'}),
            'supplier': forms.TextInput(attrs={'placeholder':'e.g. ABC','class':'form-control'}),
        }