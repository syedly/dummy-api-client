from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import product, purchase

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

class ProductForm(forms.ModelForm):
    class Meta:
        model = product
        fields = "__all__"

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = purchase
        fields = "__all__"