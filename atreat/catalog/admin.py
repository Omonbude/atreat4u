from django.contrib import admin
<<<<<<< HEAD
from .models import Restaurants, Location, Meal, Comedy, Salon, SalonDetail, Cinemas, CinemaLocation, CinemasDetail, CelebrityTest, Cbid, MusicBid, BusinessBid, TvhostBid, LogoImage
=======
from .forms import MealForm
from .models import Restaurants, Location, Meal, Comedy, Salon, SalonDetail, Cinemas, CinemaLocation, CinemasDetail, CelebrityTest, Cbid, MusicBid, BusinessBid, TvhostBid
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c

class RestaurantsAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	list_display_links = ['name']
	search_fields = ['name']
	prepopulated_fields = {'slug': ('name',)}
admin.site.register(Restaurants, RestaurantsAdmin)

class LocationAdmin(admin.ModelAdmin):
	list_display = ['address', 'Restaurant']
	list_display_links = ['address']
	search_fields = ['address', 'Restaurant']
admin.site.register(Location, LocationAdmin)




class MealAdmin(admin.ModelAdmin):
	# exclude = ['real_restaurant']
<<<<<<< HEAD
	list_display = ['restaurant', 'Menu', 'Brand', 'Size', 'Amount', 'pk', 'available']
	list_display_links = ['restaurant', 'Menu', 'Brand', 'Size']
	search_fields = ['restaurant', 'Menu', 'Brand', 'Size', 'Amount']
# 	prepopulated_fields = {'real_restaurant': ('restaurant',)}

=======
	list_display = ['restaurant', 'Menu', 'Brand', 'Size', 'Amount', 'real_restaurant', 'pk', 'location_slug' ]
	list_display_links = ['restaurant', 'Menu', 'Brand', 'Size']
	search_fields = ['restaurant', 'Menu', 'Brand', 'Size', 'Amount']
	prepopulated_fields = {'real_restaurant': ('restaurant',)}
	
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c


admin.site.register(Meal, MealAdmin)


class ComedyAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'date', 'time', 'venue', 'singles_price', 'double_price', 'round_table_price', 'vip_table_price']
	list_display_links = ['name', 'date', 'time', 'venue']
	search_fields = ['name', 'date', 'time', 'venue', 'singles_price', 'double_price', 'round_table_price', 'vip_table_price']
	prepopulated_fields = {'slug': ('name',)}


admin.site.register(Comedy, ComedyAdmin)


class CinemasAdmin(admin.ModelAdmin):
<<<<<<< HEAD
	list_display = ['name']
	list_display_links = ['name']
	search_fields = ['name']
=======
	list_display = ['name', 'venue']
	list_display_links = ['name', 'venue']
	search_fields = ['name', 'venue']
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
	prepopulated_fields = {'slug': ('name',)}
admin.site.register(Cinemas, CinemasAdmin)
admin.site.register(CinemaLocation)


class CinemasDetailAdmin(admin.ModelAdmin):
	list_display = ['cinema_name', 'movie', 'slug', 'rating', 'price', 'date', 'time', 'pk']
	list_display_links = ['cinema_name', 'movie', 'slug', 'rating', 'price', 'date', 'time']
	search_fields = ['cinema_name', 'movie', 'slug', 'rating', 'price', 'date', 'time']
	prepopulated_fields = {'slug': ('cinema_name',)}

admin.site.register(CinemasDetail, CinemasDetailAdmin)


class SalonAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'venue']
	list_display_links = ['name', 'venue']
	search_fields = ['name', 'venue']
	prepopulated_fields = {'slug': ('name',)}


admin.site.register(Salon, SalonAdmin)

class SalonDetailAdmin(admin.ModelAdmin):

	list_display = ['name', 'style', 'slug', 'gender', 'price']
	list_display_links = ['name', 'slug', 'gender', 'price']
	search_fields = ['name', 'slug', 'gender', 'price']
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(SalonDetail, SalonDetailAdmin)



class CelebrityTestAdmin(admin.ModelAdmin):
	exclude = ['slug']
	list_display = ['name', 'category', 'slug', 'charity_name', 'start', 'end']
	list_display_links = ['name', 'category', 'slug', 'charity_name']
	search_fields = ['name', 'category', 'slug', 'charity_name']
	prepopulated_fields = {'category_slug': ('category',)}

admin.site.register(CelebrityTest, CelebrityTestAdmin)
admin.site.register(Cbid)
admin.site.register(MusicBid)
admin.site.register(BusinessBid)
admin.site.register(TvhostBid)
<<<<<<< HEAD
admin.site.register(LogoImage)

=======
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
