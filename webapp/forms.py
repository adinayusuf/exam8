from django import forms
from django.forms import Textarea

from webapp.models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name_goods', 'description']
        widgets = {'description': Textarea(attrs={"rows": 1, "cols": 24})}


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['mark', 'text']
