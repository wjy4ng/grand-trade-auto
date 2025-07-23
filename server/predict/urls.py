from django.urls import path
from . import views


app_name = "predict"

urlpatterns = [
    path('predict/', views.predict_price, name='predict_price'),
]
