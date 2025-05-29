from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='user_photos/', null=True, blank=True)
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",  
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",  
        blank=True,
    )

from django import forms
from .models import CustomUser

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'photo']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class StockData(models.Model):
    ticker = models.CharField(max_length=10)  # Stock ticker symbol (e.g., TCS.BO, RELIANCE.NS)
    company_name = models.CharField(max_length=255)  # Full name of the company (e.g., Tata Consultancy Services)
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp for when the data is saved
    open_price = models.FloatField()  # Opening price
    high_price = models.FloatField()  # Highest price during the period
    low_price = models.FloatField()  # Lowest price during the period
    close_price = models.FloatField()  # Closing price at the end of the period

    def __str__(self):
        return f"{self.ticker} - {self.company_name} - {self.timestamp}"


from django.db import models

class Portfolio(models.Model):
    # Portfolio Names (Dropdown Options)
    PORTFOLIO_NAME_CHOICES = [
        ('Growth', 'Growth Portfolio'),
        ('Income', 'Income Portfolio'),
        ('Balanced', 'Balanced Portfolio'),
        ('Aggressive', 'Aggressive Portfolio'),
        ('Conservative', 'Conservative Portfolio'),
    ]

    # Stock Ticker and Company Name Choices
    STOCK_CHOICES = [
        ('RELIANCE.BO', 'Reliance Industries'),
        ('TCS.BO', 'Tata Consultancy Services'),
        ('INFY.BO', 'Infosys Limited'),
        ('HDFCBANK.BO', 'HDFC Bank'),
        ('ICICIBANK.BO', 'ICICI Bank'),
        ('ITC.BO', 'ITC Limited'),
        ('LT.BO', 'Larsen & Toubro'),
        ('SBIN.BO', 'State Bank of India'),
        ('HINDUNILVR.BO', 'Hindustan Unilever'),
        ('BAJAJFIN.BO', 'Bajaj Finance'),
    ]

    name = models.CharField(max_length=100, choices=PORTFOLIO_NAME_CHOICES)  # Portfolio name dropdown
    ticker = models.CharField(max_length=15, choices=STOCK_CHOICES)  # Increased max_length to 15
    company_name = models.CharField(max_length=100, choices=STOCK_CHOICES)  # Company name dropdown
    shares = models.PositiveIntegerField()  # Number of shares owned
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)  # Purchase price per share
    purchase_date = models.DateField()  # Date of purchase

    def __str__(self):
        return f"{self.name} - {self.company_name} ({self.ticker})"


class StockPrediction(models.Model):
    ticker = models.CharField(max_length=15)  # Stock ticker
    prediction_date = models.DateField()  # Date of the prediction
    predicted_price = models.DecimalField(max_digits=10, decimal_places=2)  # Predicted stock price

    def __str__(self):
        return f"{self.ticker} - {self.prediction_date} - {self.predicted_price}"
