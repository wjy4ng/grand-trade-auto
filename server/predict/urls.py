from django.urls import path
from . import views


app_name = "predict"

urlpatterns = [
    path('submit-form/', views.submit_form, name="submit_form"),
    path('view-result/', views.view_result, name="view_result"),
]
