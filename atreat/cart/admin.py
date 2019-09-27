from django.contrib import admin

from .models import UserCart, MealCart, UserMeal,  UserCinemas, UserSalon, UserComedySingle, UserComedyDouble, UserComedyRound, UserComedyVip, CelebrityBid, RebidCeleb
class Meal_CartAdmin(admin.ModelAdmin):
	fields = ['date_added', 'user', 'meal_product']
	list_display = ['date_added', 'user', 'meal_product']

class UserMealAdmin(admin.ModelAdmin):
<<<<<<< HEAD
	list_display = ['Menu', 'Brand', 'Size', 'price', 'location', 'real_restaurant', 'user', 'paid']
=======
	list_display = ['Menu', 'Brand', 'Size', 'price', 'location', 'real_restaurant']
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c




admin.site.register(UserCart)



admin.site.register(UserMeal, UserMealAdmin)

admin.site.register(UserComedySingle)
admin.site.register(UserComedyDouble)
admin.site.register(UserComedyRound)
admin.site.register(UserComedyVip)

admin.site.register(UserCinemas)
admin.site.register(UserSalon)
admin.site.register(CelebrityBid)

# class RebidCelebAdmin(admin.ModelAdmin):
# 	list_display = ['id', 'amount']
admin.site.register(RebidCeleb)
# admin.site.register(RebidCelebAdmin)




