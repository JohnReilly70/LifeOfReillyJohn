from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils.html import strip_tags
from django import forms

from LifeOfReillyJohn.EmailingScripts.Email import Sign_Up_Confirmation
from .forms import SignUpForm, PokemonDataBaseSearch
from .models import Pokemon

import logging
import string
import random
import re

logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


def home(request):
	return render(request=request,
	              template_name="LifeOfReillyJohnApp/home.html",
	              )


def PassGen(request):
	if request.method == "POST":
		length = int(request.POST['characters'])
		number = int(request.POST['numbers'])
		special = int(request.POST['special'])
		
		if (number + special) > length:
			p = "Password Length Must Be Greater Than Or Equal To Numbers & Special Characters Combined"
		else:
			p = []
			for _ in range(number):
				p.extend(str(random.randint(0, 9)))
			for _ in range(special):
				p.extend(random.choice(string.punctuation))
			for _ in range((length - number - special)):
				p.extend(random.choice(string.ascii_letters))
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
			
			Sign_Up_Confirmation(raw_email, username)
			
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
				              context={"form": form, "error": True})
		else:
			form = AuthenticationForm()
			return render(request=request,
			              template_name="LifeOfReillyJohnApp/LogIn.html",
			              context={"form": form, "error": True})
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


@login_required
def Profile(request):
	return render(request=request,
	              template_name="LifeOfReillyJohnApp/Profile.html",
	              )


def PokemonTable(request):
	if request.method == 'POST':
		
		search = request.POST['search'].capitalize()
		choice = request.POST['database_choice']
		
		try:
			error = False
			results = None
			
			if not search or 'Clear' in request.POST:
				results = Pokemon.objects.all()
			
			elif choice == 'Name':
				results = Pokemon.objects.filter(Name=search)
			
			elif choice == 'Type1':
				results = Pokemon.objects.filter(Type1=search)
			
			elif choice == 'Type2':
				results = Pokemon.objects.filter(Type2=search)
			
			elif choice == 'Legendary':
				results = Pokemon.objects.filter(Legendary=search)
			
			else:
				
				regex = r'^(?P<operator>=|=>|=<|>|<)?\s*(?P<integer>\d+)'
				re_result = re.match(regex, search)
				operator, search = re_result[1], int(re_result[2])
				
				if choice == 'Poke_Number':
					if operator == '=' or operator == None:
						results = Pokemon.objects.filter(Poke_Number=search)
					elif operator == '=>':
						results = Pokemon.objects.filter(Poke_Number__gte=search)
					elif operator == '=<':
						results = Pokemon.objects.filter(Poke_Number__lte=search)
					elif operator == '<':
						results = Pokemon.objects.filter(Poke_Number__lt=search)
					elif operator == '>':
						results = Pokemon.objects.filter(Poke_Number__gt=search)
				
				elif choice == 'HP':
					if operator == '=' or operator == None:
						results = Pokemon.objects.filter(HP=search)
					elif operator == '=>':
						results = Pokemon.objects.filter(HP__gte=search)
					elif operator == '=<':
						results = Pokemon.objects.filter(HP__lte=search)
					elif operator == '<':
						results = Pokemon.objects.filter(HP__lt=search)
					elif operator == '>':
						results = Pokemon.objects.filter(HP__gt=search)
				
				elif choice == 'Attack':
					if operator == '=' or operator == None:
						results = Pokemon.objects.filter(Attack=search)
					elif operator == '=>':
						results = Pokemon.objects.filter(Attack__gte=search)
					elif operator == '=<':
						results = Pokemon.objects.filter(Attack__lte=search)
					elif operator == '<':
						results = Pokemon.objects.filter(Attack__lt=search)
					elif operator == '>':
						results = Pokemon.objects.filter(Attack__gt=search)
				
				elif choice == 'Defence':
					if operator == '=' or operator == None:
						results = Pokemon.objects.filter(Defence=search)
					elif operator == '=>':
						results = Pokemon.objects.filter(Defence__gte=search)
					elif operator == '=<':
						results = Pokemon.objects.filter(Defence__lte=search)
					elif operator == '<':
						results = Pokemon.objects.filter(Defence__lt=search)
					elif operator == '>':
						results = Pokemon.objects.filter(Defence__gt=search)
				
				elif choice == 'SPAttack':
					if operator == '=' or operator == None:
						results = Pokemon.objects.filter(SPAttack=search)
					elif operator == '=>':
						results = Pokemon.objects.filter(SPAttack__gte=search)
					elif operator == '=<':
						results = Pokemon.objects.filter(SPAttack__lte=search)
					elif operator == '<':
						results = Pokemon.objects.filter(SPAttack__lt=search)
					elif operator == '>':
						results = Pokemon.objects.filter(SPAttack__gt=search)
				
				elif choice == 'SPDefence':
					if operator == '=' or operator == None:
						results = Pokemon.objects.filter(SPDefence=search)
					elif operator == '=>':
						results = Pokemon.objects.filter(SPDefence__gte=search)
					elif operator == '=<':
						results = Pokemon.objects.filter(SPDefence__lte=search)
					elif operator == '<':
						results = Pokemon.objects.filter(SPDefence__lt=search)
					elif operator == '>':
						results = Pokemon.objects.filter(SPDefence__gt=search)
				
				elif choice == 'Speed':
					if operator == '=' or operator == None:
						results = Pokemon.objects.filter(Speed=search)
					elif operator == '=>':
						results = Pokemon.objects.filter(Speed__gte=search)
					elif operator == '=<':
						results = Pokemon.objects.filter(Speed__lte=search)
					elif operator == '<':
						results = Pokemon.objects.filter(Speed__lt=search)
					elif operator == '>':
						results = Pokemon.objects.filter(Speed__gt=search)
				
				elif choice == 'Generation':
					if operator == '=' or operator == None:
						results = Pokemon.objects.filter(Generation=search)
					elif operator == '=>':
						results = Pokemon.objects.filter(Generation__gte=search)
					elif operator == '=<':
						results = Pokemon.objects.filter(Generation__lte=search)
					elif operator == '<':
						results = Pokemon.objects.filter(Generation__lt=search)
					elif operator == '>':
						results = Pokemon.objects.filter(Generation__gt=search)
			
			if not results:
				error = True
			
			return render(request=request,
			              template_name="LifeOfReillyJohnApp/Pokemon.html",
			              context={"PokemonList": results,
			                       "PokemonDataBaseSearch": PokemonDataBaseSearch(),
			                       "error": error,
			                       }
			              )
		except:
			return render(request=request,
			              template_name="LifeOfReillyJohnApp/Pokemon.html",
			              context={"PokemonList": results,
			                       "PokemonDataBaseSearch": PokemonDataBaseSearch(),
			                       "error": True,
			                       }
			              )
	
	return render(request=request,
	              template_name="LifeOfReillyJohnApp/Pokemon.html",
	              context={"PokemonList": Pokemon.objects.all(),
	                       "PokemonDataBaseSearch": PokemonDataBaseSearch,
	                       }
	              )


def Graphs(request):
	gen1 = len(Pokemon.objects.filter(Generation=1))
	gen2 = len(Pokemon.objects.filter(Generation=2))
	gen3 = len(Pokemon.objects.filter(Generation=3))
	gen4 = len(Pokemon.objects.filter(Generation=4))
	gen5 = len(Pokemon.objects.filter(Generation=5))
	gen6 = len(Pokemon.objects.filter(Generation=6))
	return render(request=request,
	              template_name="LifeOfReillyJohnApp/Graphs.html",
	              context={"gen1": gen1,
	                       "gen2": gen2,
	                       "gen3": gen3,
	                       "gen4": gen4,
	                       "gen5": gen5,
	                       "gen6": gen6, }
	              )
