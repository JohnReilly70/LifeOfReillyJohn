from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, decorators, logout
from LifeOfReillyJohn.EmailingScripts.Email import Sign_Up_Confirmation


import logging
import os
import string
import random
from .forms import SignUpForm, LogInForm


logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')



def home(request):
    return render(request=request,
              template_name="LifeOfReillyJohnApp/home.html",
              )


def PassGen(request):
    if request.method == "POST":
        length = int(request.POST['characters'])
        upper = int(request.POST['numbers'])
        special = int(request.POST['special'])

        if (upper+special) > length:
            p = "Password Length Must Be Greater Than Or Equal To Numbers & Special Characters Combined"
        else:
            p = []
            for _ in range(upper):
                p.extend(random.choice(string.ascii_uppercase))
            for _ in range(special):
                p.extend(random.choice(string.punctuation))
            for _ in range((length - upper - special)):
                p.extend(random.choice(string.ascii_letters + string.digits + string.punctuation))
            random.shuffle(p)
            p = "".join(p)




        return render(request=request,
                      template_name="LifeOfReillyJohnApp/PassGen.html",
                      context={"password": p}
                      )
    else:
        return render(request=request,
                      template_name="LifeOfReillyJohnApp/PassGen.html",
                      context={})


def FontGen(request):
   return render(request=request,
              template_name="LifeOfReillyJohnApp/FontGen.html",
              )


def SignUp(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            raw_email = form.cleaned_data.get('email')
            
            
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            
            Sign_Up_Confirmation("C:/Users/johnr/Desktop/pythonanywhere/LifeOfReillyJohn/LifeOfReillyJohnApp/credentials.txt",raw_email, username)

            return render(request=request,
                      template_name="LifeOfReillyJohnApp/home.html",
                      context=({'SignUpValid': {'UserName': username}})
                      )
    else:
        form = SignUpForm()

    return render(request=request,
                  template_name="LifeOfReillyJohnApp/SignUp.html",
                  context=({'form': form})
                  )

def LogIn(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request=request,
                              template_name="LifeOfReillyJohnApp/home.html",
                              context=({})
                              )
            else:
                form = AuthenticationForm()
                return render(request=request,
                              template_name="LifeOfReillyJohnApp/LogIn.html",
                              context={"form": form,"error": True})
        else:
            form = AuthenticationForm()
            return render(request=request,
                          template_name="LifeOfReillyJohnApp/LogIn.html",
                          context={"form": form,"error": True})
    else:
        form = AuthenticationForm()
        return render(request=request,
                  template_name="LifeOfReillyJohnApp/LogIn.html",
                  context={"form": form})

def LogOut(request):
    logout(request)
    return render(request=request,
                  template_name="LifeOfReillyJohnApp/home.html",
                  context=({})
                  )