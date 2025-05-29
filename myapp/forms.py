from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserRegistrationForm(UserCreationForm):
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password',
        })
    )

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'photo', 'email', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name',
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username',
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address',
            }),
            
        }

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'})
    )

from django import forms
from .models import Portfolio

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['name', 'ticker', 'company_name', 'shares', 'purchase_price', 'purchase_date']
        widgets = {
            'name': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select Portfolio Type'}),
            'ticker': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select Stock Ticker'}),
            'company_name': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select Company'}),
            'shares': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number of shares'}),
            'purchase_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter purchase price'}),
            'purchase_date': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Select purchase date',
                'type': 'date',
            }),
        }
