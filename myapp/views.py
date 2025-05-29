from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from .utils import *


def base(request):
    return render(request, 'base.html')

def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful!")
            return redirect('login')
        else:
            messages.error(request, "Error during registration.")
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('home')
        messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')


# Admin
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import UserRegistrationForm

CustomUser = get_user_model()

@login_required
def user_list(request):
    """
    List all users.
    """
    users = CustomUser.objects.all()
    return render(request, 'user/user_list.html', {'users': users})

@login_required
def user_create(request):
    """
    Create a new user.
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully.")
            return redirect('user_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'user/user_form.html', {'form': form, 'title': 'Create User'})

@login_required
def user_update(request, pk):
    """
    Update an existing user.
    """
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User updated successfully.")
            return redirect('user_list')
    else:
        form = UserRegistrationForm(instance=user)
    return render(request, 'user/user_form.html', {'form': form, 'title': 'Update User'})

@login_required
def user_delete(request, pk):
    """
    Delete a user.
    """
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request, "User deleted successfully.")
        return redirect('user_list')
    return render(request, 'user/user_confirm_delete.html', {'user': user})

# user
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import UserRegistrationForm

CustomUser = get_user_model()

@login_required
def user_profile(request):
    """
    Display the logged-in user's profile.
    """
    return render(request, 'user/profile.html', {'user': request.user})

@login_required

@login_required
def update_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after updating
    else:
        form = UserProfileForm(instance=user)
    
    return render(request, 'user/update_profile.html', {'form': form})

@login_required
def delete_profile(request):
    """
    Allow the logged-in user to delete their profile.
    """
    user = request.user
    if request.method == 'POST':
        user.delete()
        messages.success(request, "Your profile has been deleted.")
        return redirect('home')  # Redirect to home or login page
    return render(request, 'user/profile_confirm_delete.html')


# 2021453
# stocks/views.py
from django.shortcuts import render
from .models import StockData
from django.db.models import Q
from django.utils.dateformat import DateFormat

def stock_data_list(request):
    query = request.GET.get('query', '')  # Search by ticker or company name
    date_from = request.GET.get('date_from', '')  # Start date for filtering
    date_to = request.GET.get('date_to', '')  # End date for filtering

    # Filter data
    stock_data = StockData.objects.all()


    if query:
        stock_data = stock_data.filter(
            Q(ticker__icontains=query) | Q(company_name__icontains=query)
        )

    if date_from:
        stock_data = stock_data.filter(timestamp__date__gte=date_from)

    if date_to:
        stock_data = stock_data.filter(timestamp__date__lte=date_to)

    # Prepare data for Chart.js
    chart_labels = [DateFormat(stock.timestamp).format('Y-m-d') for stock in stock_data]
    open_prices = [stock.open_price for stock in stock_data]
    close_prices = [stock.close_price for stock in stock_data]
    high_prices = [stock.high_price for stock in stock_data]
    low_prices = [stock.low_price for stock in stock_data]

    context = {
        'stock_data': stock_data,
        'query': query,
        'date_from': date_from,
        'date_to': date_to,
        'chart_labels': chart_labels,
        'open_prices': open_prices,
        'close_prices': close_prices,
        'high_prices': high_prices,
        'low_prices': low_prices,
    }
    return render(request, 'stocks/stock_data_list.html', context)

from django.shortcuts import get_object_or_404

def stock_detail(request, pk):
    stock = get_object_or_404(StockData, pk=pk)

    # Profit/Loss Prediction
    profit_loss = "Profit" if stock.close_price > stock.open_price else "Loss"
    profit_loss_amount = abs(stock.close_price - stock.open_price)

    context = {
        'stock': stock,
        'profit_loss': profit_loss,
        'profit_loss_amount': profit_loss_amount,
    }
    return render(request, 'stocks/stock_detail.html', context)

# portfolio....
from django.shortcuts import render, get_object_or_404, redirect
from .models import Portfolio
from .forms import PortfolioForm

# List all portfolios
def portfolio_list(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'portfolio/portfolio_list.html', {'portfolios': portfolios})

# Add a new portfolio
def portfolio_add(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio_list')
    else:
        form = PortfolioForm()
    return render(request, 'portfolio/portfolio_form.html', {'form': form})

# Edit an existing portfolio
def portfolio_edit(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('portfolio_list')
    else:
        form = PortfolioForm(instance=portfolio)
    return render(request, 'portfolio/portfolio_form.html', {'form': form})

# Delete a portfolio
def portfolio_delete(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    if request.method == 'POST':
        portfolio.delete()
        return redirect('portfolio_list')
    return render(request, 'portfolio/portfolio_confirm_delete.html', {'portfolio': portfolio})

# pricePrediction
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from .models import StockData, StockPrediction
from .utils import predict_prices_for_ticker
from django.conf import settings
import json

def generate_predictions(request):
    """
    Generate price predictions for the next 7 days for all unique tickers and send a report via email.
    """
    if request.method == 'POST':
        tickers = StockData.objects.values_list('ticker', flat=True).distinct()
        errors = []
        predictions_list = []
        candlestick_data = []  # Data for visualization
        email_report = []

        for ticker in tickers:
            try:
                predictions = predict_prices_for_ticker(ticker)
                predictions_list.append({ticker: predictions})

                # Prepare candlestick data for the ticker
                historical_data = StockData.objects.filter(ticker=ticker).order_by('timestamp')
                candlestick_data.append({
                    "ticker": ticker,
                    "dates": [data.timestamp.strftime("%Y-%m-%d") for data in historical_data],
                    "opens": [data.open_price for data in historical_data],
                    "highs": [data.high_price for data in historical_data],
                    "lows": [data.low_price for data in historical_data],
                    "closes": [data.close_price for data in historical_data],
                })

                # Add prediction to email report
                email_report.append(f"<h3>{ticker}</h3>")
                email_report.append("<table border='1'><tr><th>Date</th><th>Predicted Price</th></tr>")
                for prediction in predictions:
                    email_report.append(f"<tr><td>{prediction['date']}</td><td>₹{prediction['price']}</td></tr>")
                email_report.append("</table>")
            except Exception as e:
                errors.append(f"Error predicting for {ticker}: {e}")

        # Send email report if predictions are generated
        if predictions_list:
            email_body = "<h1>Stock Price Predictions</h1>" + "".join(email_report)
            send_mail(
                subject="Stock Price Predictions Report",
                message="",
                html_message=email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[request.user.email],  # Send to the logged-in user
                fail_silently=False,
            )

        if errors:
            messages.error(request, "Some predictions could not be generated.")
        else:
            messages.success(request, "Predictions generated successfully! Report sent to your email.")

        return render(
            request,
            'price/price_prediction.html',
            {
                'predictions_list': predictions_list,
                'candlestick_data': json.dumps(candlestick_data),
                'errors': errors,
            },
        )
    
    # If GET request
    return render(request, 'price/price_prediction.html', {})

def graph(request):
    return render(request, 'stocks/graph.html')
