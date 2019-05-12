from django.shortcuts import render

# Create your views here.

def home(request):
   return render(request=request,
              template_name="LifeOfReillyJohnApp/home.html",
              )


def PassGen(request):
   return render(request=request,
              template_name="LifeOfReillyJohnApp/PassGen.html",
              )