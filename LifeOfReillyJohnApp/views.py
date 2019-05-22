from django.shortcuts import render
import string
import random
# Create your views here.

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

