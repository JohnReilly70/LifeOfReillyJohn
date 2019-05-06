from django.urls import path, include
from . import views

app_name = "LifeOfReillyJohnApp"

urlpatterns = [
    path("", views.home, name="homepage"),
]
