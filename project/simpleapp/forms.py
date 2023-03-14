from django import forms
from django.core.exceptions import ValidationError

from .models import Product


class ProductForm(forms.ModelForm):
   class Meta:
       model = Product
       fields = ['name', 'description', 'category', 'price', 'quantity']

       def clean(self):
           cleaned_data = super().clean()
           description = cleaned_data.get("description")
           name = cleaned_data.get("name")

           if name == description:
               raise ValidationError(
                   "The description should not be identical to the name."
               )

           return cleaned_data