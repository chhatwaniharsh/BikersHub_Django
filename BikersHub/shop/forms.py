from .models import Product, Contact
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'