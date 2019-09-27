from django.db import models
from django.contrib.auth.models import User
from catalog.models import Meal, Comedy, CinemasDetail, SalonDetail


class MealCart(models.Model):
<<<<<<< HEAD
	# user = models.OneToOneField(User, on_delete=models.CASCADE)
=======
	# user = models.OneToOneField(User, on_delete=models.CASCADE) 
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
	detail = models.CharField(max_length=50)
	def __str__(self):
		return self.detail
class UserMeal(models.Model):
	real_restaurant = models.CharField(max_length=50)
	# real_restaurant = models.CharField(max_length=50)
<<<<<<< HEAD

=======
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
	location = models.CharField(max_length=50)
	Menu= models.CharField(max_length=50)
	Brand= models.CharField(max_length=50, null=True, blank=True)
	Size= models.CharField(max_length=50, null=True, blank=True)
	price= models.DecimalField(max_length=50, decimal_places=2, max_digits=15)
	user = models.CharField(max_length=50)
	quantity = models.IntegerField(default=1)
	Total_price = models.CharField(max_length=50, default=0)
<<<<<<< HEAD
	date = models.DateTimeField(auto_now_add=True, blank=True)
	paid = models.BooleanField(default=False)
=======
	date = models.DateTimeField(auto_now_add=True, blank=True)	
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c

	def __str__(self):
		return self.Menu


class MealQuantity(models.Model):
	quantity = models.IntegerField()
class CinemaQuantity(models.Model):
	quantity = models.IntegerField()

class UserCart(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.user.username

class UserCinemas(models.Model):
	cinema_name = models.CharField(max_length=200)
<<<<<<< HEAD
	location = models.CharField(max_length=200)
=======
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
	movie = models.CharField(max_length=200)
	slug = models.SlugField()
	image = models.ImageField()
	rating = models.CharField(max_length=200)
<<<<<<< HEAD
	price = models.DecimalField(max_length=50, decimal_places=2, max_digits=15)
	date = models.CharField(max_length=200)
	time = models.CharField(max_length=200)
	user = models.CharField(max_length=50)
	date = models.DateTimeField(auto_now_add=True, blank=True)
	paid = models.BooleanField(default=False)
=======
	price = models.DecimalField(max_length=50, decimal_places=2, max_digits=15)	
	date = models.CharField(max_length=200)
	time = models.CharField(max_length=200)
	user = models.CharField(max_length=50)
	date = models.DateTimeField(auto_now_add=True, blank=True)	
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c

	def __str__(self):
		return self.slug


class UserComedySingle(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	image = models.ImageField()
	date = models.DateField()
	time = models.CharField(max_length=10)
	venue = models.CharField(max_length=200)
	singles_price = models.DecimalField(max_length=50, decimal_places=2, max_digits=15)
	category = models.CharField(max_length=30, default='Singles')
	user = models.CharField(max_length=50)
<<<<<<< HEAD
	date = models.DateTimeField(auto_now_add=True, blank=True)
	paid = models.BooleanField(default=False)
	def __str__(self):
		return self.name
=======
	date = models.DateTimeField(auto_now_add=True, blank=True)	
	def __str__(self):
		return self.name	
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c

class UserComedyDouble(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	image = models.ImageField()
	date = models.DateField()
	time = models.CharField(max_length=10)
	venue = models.CharField(max_length=200)
	double_price = models.DecimalField(max_length=50, decimal_places=2, max_digits=15)
	category = models.CharField(max_length=30, default='Double')
	user = models.CharField(max_length=50)
<<<<<<< HEAD
	date = models.DateTimeField(auto_now_add=True, blank=True)
	paid = models.BooleanField(default=False)
	def __str__(self):
		return self.name
=======
	date = models.DateTimeField(auto_now_add=True, blank=True)	
	def __str__(self):
		return self.name	
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c

class UserComedyRound(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	image = models.ImageField()
	date = models.DateField()
	time = models.CharField(max_length=10)
	venue = models.CharField(max_length=200)
<<<<<<< HEAD
	round_table_price = models.DecimalField(max_length=50, decimal_places=2, max_digits=15)
	category = models.CharField(max_length=30, default='Round Table')
	user = models.CharField(max_length=50)
	date = models.DateTimeField(auto_now_add=True, blank=True)
	paid = models.BooleanField(default=False)
	def __str__(self):
		return self.name


=======
	round_table_price = models.DecimalField(max_length=50, decimal_places=2, max_digits=15)	
	category = models.CharField(max_length=30, default='Round Table')
	user = models.CharField(max_length=50)
	date = models.DateTimeField(auto_now_add=True, blank=True)	
	def __str__(self):
		return self.name	

	
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
class UserComedyVip(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	image = models.ImageField()
	date = models.DateField()
	time = models.CharField(max_length=10)
	venue = models.CharField(max_length=200)
<<<<<<< HEAD
	vip_table_price = models.DecimalField(max_length=50, decimal_places=2, max_digits=15)
	category = models.CharField(max_length=30, default='Vip Table')
	user = models.CharField(max_length=50)
	date = models.DateTimeField(auto_now_add=True, blank=True)
	paid = models.BooleanField(default=False)
	def __str__(self):
		return self.name




=======
	vip_table_price = models.DecimalField(max_length=50, decimal_places=2, max_digits=15)	
	category = models.CharField(max_length=30, default='Vip Table')
	user = models.CharField(max_length=50)
	date = models.DateTimeField(auto_now_add=True, blank=True)	
	def __str__(self):
		return self.name	

	
	
	
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c



class UserSalon(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField()
	style = models.CharField(max_length=200)
	image = models.ImageField()
	gender = models.CharField(max_length=100)
<<<<<<< HEAD
	price = models.DecimalField(max_length=50, decimal_places=2, max_digits=15)
	user = models.CharField(max_length=50)
	date = models.DateTimeField(auto_now_add=True, blank=True)
	paid = models.BooleanField(default=False)
=======
	price = models.DecimalField(max_length=50, decimal_places=2, max_digits=15)	
	user = models.CharField(max_length=50)
	date = models.DateTimeField(auto_now_add=True, blank=True)	
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c

	def __str__(self):
		return self.style

class CelebrityBid(models.Model):
	user = models.CharField(max_length=50, default=User)
	amount = models.DecimalField(max_length=50, decimal_places=2, max_digits=15)
<<<<<<< HEAD
	paid = models.BooleanField(default=False)

=======
	
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
	def __str__(self):
		return self.user

class RebidCeleb(models.Model):
<<<<<<< HEAD
	user = models.CharField(max_length=50, default=User)
	amount = models.DecimalField(max_length=50, decimal_places=2, max_digits=15, default=0.00)
	celeb = models.CharField(max_length=50, default='none')
	paid = models.BooleanField(default=False)
=======
	user = models.CharField(max_length=50, default=User) 
	amount = models.DecimalField(max_length=50, decimal_places=2, max_digits=15, default=0.00)
	celeb = models.CharField(max_length=50, default='none') 
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
	def __str__(self):
		return self.user