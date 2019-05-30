from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

app_name = "LifeOfReillyJohnApp"

urlpatterns = [
    path("PassGen/", views.PassGen, name="PassGen"),
    path("FontGen/", views.FontGen, name="FontGen"),
    path("SignUp/", views.SignUp, name="SignUp"),
    path("LogOut/", views.LogOut, name="LogOut"),
    path("LogIn/", views.LogIn, name="LogIn"),
    path('password-reset/', auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset.html',
            email_template_name='registration/password_reset_email.html',
            success_url=reverse_lazy('LifeOfReillyJohnApp:password_reset_done')
        ),
        name='password_reset'),
    
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'
         ),
         name='password_reset_done'),

    
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html',
            success_url=reverse_lazy('LifeOfReillyJohnApp:password_reset_complete')
         ),
         name='password_reset_confirm'),
    
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    
    path("", views.home, name="home"),
    

]
