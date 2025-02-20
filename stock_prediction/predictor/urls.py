from django.urls import path
from .views import predict_stock_price, first_page
from .views import signup_view, login_view

urlpatterns = [
    path("", first_page, name="home"),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path("stock/", predict_stock_price, name="predict_stock"),
]
