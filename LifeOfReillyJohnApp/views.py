from django.shortcuts import render
from django.contrib.auth import login, authenticate, decorators

import string
import random
from .forms import SignUpForm

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

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print("entered")
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request=request,
                      template_name="LifeOfReillyJohnApp/home.html",
                      context=({'SignUpValid': {'UserName': username}})
                      )

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUpForm()

    return render(request=request,
                  template_name="LifeOfReillyJohnApp/SignUp.html",
                  context=({'form': form})
                  )