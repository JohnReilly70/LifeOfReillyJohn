from django.db import models

# Create your models here.


class Pokemon(models.Model):
	
	
	class Meta:
		ordering = ['Poke_Number']
		
		
	Poke_Number = models.IntegerField()
	Name = models.CharField(max_length=50)
	Type1 = models.CharField(max_length=50)
	Type2 = models.CharField(max_length=50)
	HP = models.IntegerField(default=0)
	Attack = models.IntegerField(default=0)
	Defence = models.IntegerField(default=0)
	SPAttack = models.IntegerField(default=0)
	SPDefence = models.IntegerField(default=0)
	Speed = models.IntegerField(default=0)
	Generation = models.IntegerField(default=1)
	Legendary = models.BooleanField(default=False)
	
	

	
	def __str__(self):
		return f'{self.Poke_Number}: {self.Name}'