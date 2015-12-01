from django.forms import ModelForm, Textarea, TextInput
from django.forms.widgets import PasswordInput, DateInput
from ecommerce.models import Customer, Cart

__author__ = 'hakim'


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('email', 'name', 'address', 'birth_date', 'gender', 'password')
        widgets = {
            'email': TextInput({'class': 'form-control', 'placeholder': 'E-Mail'}),
            'password': PasswordInput({'class': 'form-control'}),
            'name': TextInput({'class': 'form-control'}),
            'birth_date': DateInput({'class': 'form-control'}),
            'address': Textarea({'rows': 3, 'class': 'form-control'}),
        }


class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = ('delivery_name', 'delivery_address', 'payment_method', 'created_by')
        widgets = {
            'delivery_name': TextInput({'class': 'form-control'}),
            'delivery_address': Textarea({'rows': 3, 'class': 'form-control'}),
        }
