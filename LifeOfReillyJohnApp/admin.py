from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Pokemon
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.

class PokemonInfoAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Pokemon", {'fields': ['Poke_Number', 'Name', 'Generation', 'Legendary']}),
	    ("Stats", {'fields': ['Type1', 'Type2', 'HP', 'Attack', 'Defence', 'SPAttack', 'SPDefence', 'Speed']})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

# Register your models here.
admin.site.register(Pokemon, PokemonInfoAdmin)