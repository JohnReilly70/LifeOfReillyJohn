from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. A valid email address.')
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class LogInForm(AuthenticationForm):
    
    class Meta:
        model = User
        

class PokemonDataBaseSearch(forms.Form):
    
        
    choice = (
        ('Poke_Number', 'Pokedex Number'),
        ('Name', 'Name'),
        ('Type1', 'Type1'),
        ('Type2', 'Type2'),
        ('HP', 'HP'),
        ('Attack', 'Attack'),
        ('Defence', 'Defence'),
        ('SPAttack', 'SPAttack'),
        ('SPDefence', 'SPDefence'),
        ('Speed', 'Speed'),
        ('Generation', 'Generation'),
        ('Legendary', 'Legendary'),
    )
    
    
    search = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search Database'}), required=False)
    database_choice = forms.MultipleChoiceField(widget=forms.Select, choices=choice, required=False)