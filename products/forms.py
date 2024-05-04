from django.forms import ModelForm
from .models import Phones

class ProductForm(ModelForm):
    class Meta:
        model=Phones
        fields='__all__'