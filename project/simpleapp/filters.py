from django_filters import FilterSet, ModelChoiceFilter
from .models import Product, Material

class ProductFilter(FilterSet):
    material = ModelChoiceFilter(
        field_name='productmaterial__material',
        queryset=Material.objects.all(),
        label='Material',
        empty_label='Any'
    )

    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            'quantity': ['gt'],
            'price': ['lt', 'gt'],
        }
