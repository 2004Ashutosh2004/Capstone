import pickle
import numpy as np
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import StockPrediction
from sklearn.preprocessing import StandardScaler
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

# Load the model and scaler
with open("stock_price_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)


def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Sign up successfully!")
        return redirect('home')

    return render(request, 'predictor/signup.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('predict_stock')  # Redirect to the stock prediction page
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'predictor/login.html')

def first_page(request):
    return render(request, "predictor/index.html")

def predict_stock_price(request):
    if request.method == "POST":
        try:
            # Get user input
            data = request.POST
            open_price = float(data.get("open"))
            high = float(data.get("high"))
            low = float(data.get("low"))
            pe = float(data.get("pe"))
            pb = float(data.get("pb"))
            div_yield = float(data.get("div_yield"))

            # Prepare input data
            features = np.array([[open_price, high, low, pe, pb, div_yield]])

            # Apply scaling
            features_scaled = scaler.transform(features)

            # Make prediction
            predicted_price = model.predict(features_scaled)[0]

            # Save data to database
            prediction = StockPrediction(
                open_price=open_price,
                high=high,
                low=low,
                pe_ratio=pe,
                pb_ratio=pb,
                dividend_yield=div_yield,
                predicted_close_price=round(predicted_price, 2)
            )
            prediction.save()

            # Return JSON response for AJAX
            return JsonResponse({"predicted_close_price": round(predicted_price, 2)})

        except Exception as e:
            return JsonResponse({"error": str(e)})

    return render(request, "predictor/stock.html")
