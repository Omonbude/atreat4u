from django.db import models
from django.utils.text import slugify
<<<<<<< HEAD
from datetime import datetime
=======
from datetime import datetime  
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c

class Restaurants(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField()
	image = models.ImageField()
	def __str__(self):
		return self.slug


class Location(models.Model):
	Restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE, related_name='restaurant_location')
	address = models.CharField(max_length=200)
	def __str__(self):
		return self.address


class Meal(models.Model):
	size_choice = (('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large'))
	restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE, related_name='restaurants')
<<<<<<< HEAD
# 	real_restaurant = models.CharField(max_length=50)
	location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='location1')
# 	location_slug = models.SlugField()
=======
	real_restaurant = models.CharField(max_length=50)
	location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='location1')
	location_slug = models.SlugField()
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
	Menu= models.CharField(max_length=50)
	Brand= models.CharField(max_length=50, null=True, blank=True)
	Size= models.CharField(max_length=50, choices=size_choice, null=True, blank=True)
	Amount= models.DecimalField(max_length=50, decimal_places=2, max_digits=15)
<<<<<<< HEAD
	available = models.BooleanField(default=True)
	#def save(self, *args, **kwargs):
		#self.real_restaurant = slugify(self.restaurant)
# 		self.location_slug = self.location
		# print(self.real_restaurant)
		#super (Meal, self).save(*args, **kwargs)
=======
	def save(self, *args, **kwargs):
		self.real_restaurant = slugify(self.restaurant)
		self.location_slug = slugify(self.location)
		# print(self.real_restaurant)
		super (Meal, self).save(*args, **kwargs)
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
	def __str__(self):
		return self.Menu
	# class Meta:
	# 	# ordering = ('name', )
	# 	# self.real_restaurant = slugify(self.restaurant)

	#     index_together = (('id', 'real_restaurant'))


class Comedy(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	image = models.ImageField()
	date = models.DateField()
	time = models.CharField(max_length=10)
	venue = models.CharField(max_length=200)
<<<<<<< HEAD
	singles_price = models.DecimalField(max_length=50, decimal_places=2, max_digits=15)
=======
	singles_price = models.DecimalField(max_length=50, decimal_places=2, max_digits=15)	
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
	double_price = models.DecimalField(max_length=50, decimal_places=2, max_digits=15)
	round_table_price = models.DecimalField(max_length=50, decimal_places=2, max_digits=15)
	vip_table_price = models.DecimalField(max_length=50, decimal_places=2, max_digits=15)
	def __str__(self):
		return self.name


class Cinemas(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	image = models.ImageField()
<<<<<<< HEAD
# 	venue = models.CharField(max_length=200)
=======
	venue = models.CharField(max_length=200)
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c

	def __str__(self):
		return self.name
class CinemaLocation(models.Model):
<<<<<<< HEAD
    cinema = models.ForeignKey(Cinemas, on_delete=models.CASCADE, related_name='cinema_location')
    address = models.CharField(max_length=200)
    available = models.BooleanField(default=True)
    def __str__(self):
        return self.address

class CinemasDetail(models.Model):
    cinema_name = models.ForeignKey(Cinemas, on_delete=models.CASCADE, related_name='cinema_name')
    movie = models.CharField(max_length=200)
    location = models.ForeignKey(CinemaLocation, on_delete=models.CASCADE, related_name='cinema_location')
    slug = models.SlugField()
    image = models.ImageField()
    rating = models.CharField(max_length=200)
    price = models.DecimalField(max_length=50, decimal_places=2, max_digits=15)
    date = models.DateField()
    time = models.CharField(max_length=10)
    available = models.BooleanField(default=True)


    def save(self, *args, **kwargs):
    	# self.slug = self.cinema_name
    	self.slug = slugify(self.movie)
    	super (CinemasDetail, self).save(*args, **kwargs)
    def __str__(self):
        return self.slug
=======
	cinema = models.ForeignKey(Cinemas, on_delete=models.CASCADE, related_name='cinema_location')
	address = models.CharField(max_length=200)
	def __str__(self):
		return self.address

class CinemasDetail(models.Model):
	cinema_name = models.ForeignKey(Cinemas, on_delete=models.CASCADE, related_name='cinema_name')
	movie = models.CharField(max_length=200)
	slug = models.SlugField()
	image = models.ImageField()
	rating = models.CharField(max_length=200)
	price = models.DecimalField(max_length=50, decimal_places=2, max_digits=15)	
	date = models.DateField()
	time = models.CharField(max_length=10)
	

	def save(self, *args, **kwargs):
		# self.slug = self.cinema_name
		self.slug = slugify(self.movie)
		super (CinemasDetail, self).save(*args, **kwargs)
	def __str__(self):
		return self.slug
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c



class Salon(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	image = models.ImageField()
	venue = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class SalonDetail(models.Model):
	gender_choice = (('M', 'Male'), ('F', 'Female'))
	name = models.ForeignKey(Salon, on_delete=models.CASCADE, related_name='salon_name')
	slug = models.SlugField()
	style = models.CharField(max_length=200)
	image = models.ImageField()
	gender = models.CharField(choices=gender_choice, max_length=10)
<<<<<<< HEAD
	price = models.DecimalField(max_length=50, decimal_places=2, max_digits=15)
=======
	price = models.DecimalField(max_length=50, decimal_places=2, max_digits=15)	
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c

	# def save(self, *args, **kwargs):
	# 	self.slug = slugify(self.name)
	# 	super (SalonDetail, self).save(*args, **kwargs)
	def __str__(self):
		return self.slug



class CelebrityTest(models.Model):
	category_choice = (('Nollywood Celebrities', 'Nollywood Celebrities'), ('musical Artist Celebrities', 'musical Artist Celebrities'),
		('Business Icon Celebrities', 'Business Icon Celebrities'), ('TV Host Celebrities', 'TV Host Celebrities')
	 )
	name = models.CharField(max_length=100)
	image = models.ImageField()
	category = models.CharField(max_length=100, choices = category_choice)
	category_slug = models.SlugField()
	movie = models.FileField()
	slug= models.SlugField()
	charity_name = models.CharField(max_length=100)
	charity_image = models.ImageField()
	treat_description = models.CharField(max_length=500)
<<<<<<< HEAD
	start_bid = models.DecimalField(max_length=50, decimal_places=2, max_digits=15, default=5000.00)
	start = models.DateTimeField()
	end = models.DateTimeField()
=======
	start = models.DateTimeField(auto_now_add=True, blank=True)
	end = models.DateTimeField(auto_now_add=True, blank=True)
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		self.category_slug  = slugify(self.category)
		super (CelebrityTest, self).save(*args, **kwargs)

	def __str__(self):
<<<<<<< HEAD
		return self.name
=======
		return self.name 
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c

class Cbid(models.Model):
# this is the movie bid model
	user = models.CharField(max_length=100, default='none')
	celeb = models.CharField(max_length=100, default='none')
	amount = models.DecimalField(max_length=50, decimal_places=2, max_digits=15, default=0.00)
<<<<<<< HEAD
	#The amount to pay is done when you've subtracted the old amount from the new amount
	amount_to_pay = models.DecimalField(max_length=50, decimal_places=2, max_digits=15, default=0.00)
	date = models.DateTimeField(auto_now_add=True, blank=True)
	paid = models.BooleanField(default=False)
	new_amount = models.DecimalField(max_length=50, decimal_places=2, max_digits=15, default=0.00) #new amount after payment have been done
	new_amount_paid = models.BooleanField(default=False) #true after payment
	def __str__(self):
		return self.user
=======
	date = models.DateTimeField(auto_now_add=True, blank=True)	
	def __str__(self):
		return self.user 
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c



class MusicBid(models.Model):
	user = models.CharField(max_length=100, default='none')
	celeb = models.CharField(max_length=100, default='none')
	amount = models.DecimalField(max_length=50, decimal_places=2, max_digits=15, default=0.00)
<<<<<<< HEAD
	date = models.DateTimeField(auto_now_add=True, blank=True)
	paid = models.BooleanField(default=False)
	new_amount = models.DecimalField(max_length=50, decimal_places=2, max_digits=15, default=0.00) #new amount after payment have been done
	new_amount_paid = models.BooleanField(default=False) #true after payment


	def __str__(self):
		return self.user
=======
	date = models.DateTimeField(auto_now_add=True, blank=True)	
	def __str__(self):
		return self.user 
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
class BusinessBid(models.Model):
	user = models.CharField(max_length=100, default='none')
	celeb = models.CharField(max_length=100, default='none')
	amount = models.DecimalField(max_length=50, decimal_places=2, max_digits=15, default=0.00)
<<<<<<< HEAD
	date = models.DateTimeField(auto_now_add=True, blank=True)
	paid = models.BooleanField(default=False)
	new_amount = models.DecimalField(max_length=50, decimal_places=2, max_digits=15, default=0.00) #new amount after payment have been done
	new_amount_paid = models.BooleanField(default=False) #true after payment
	def __str__(self):
		return self.user
=======
	date = models.DateTimeField(auto_now_add=True, blank=True)	
	def __str__(self):
		return self.user 
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
class TvhostBid(models.Model):
	user = models.CharField(max_length=100, default='none')
	celeb = models.CharField(max_length=100, default='none')
	amount = models.DecimalField(max_length=50, decimal_places=2, max_digits=15, default=0.00)
<<<<<<< HEAD
	date = models.DateTimeField(auto_now_add=True, blank=True)
	paid = models.BooleanField(default=False)
	new_amount = models.DecimalField(max_length=50, decimal_places=2, max_digits=15, default=0.00) #new amount after payment have been done
	new_amount_paid = models.BooleanField(default=False) #true after payment
	def __str__(self):
		return self.user
#this model is used to temporary store restaurant name and location before adding to cart
class RestaurantData(models.Model):
    restaurant = models.CharField(max_length=2000, blank=True, null=True)
    location = models.CharField(max_length=2000, blank=True, null=True)
    # def __str__(self):
    # 	return self.restaurant

#this model is used to temporary store cinema name and location before adding to cart
class CinemaData(models.Model):
    cinema = models.CharField(max_length=2000, blank=True, null=True)
    location = models.CharField(max_length=2000, blank=True, null=True)

class LogoImage(models.Model):
	image = models.FileField()
=======
	date = models.DateTimeField(auto_now_add=True, blank=True)	
	def __str__(self):
		return self.user 
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
