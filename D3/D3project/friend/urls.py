# friend/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("login_guard/", views.login_view, name="login_guard"),
    path("login_senior/", views.login_senior_view, name="login_senior")
]
