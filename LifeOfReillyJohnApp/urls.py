from django.urls import path, include
from . import views

app_name = "LifeOfReillyJohnApp"

urlpatterns = [
    path("PassGen/", views.PassGen, name="PassGen"),
    path("FontGen/", views.FontGen, name="FontGen"),
    path("", views.home, name="home"),

]
