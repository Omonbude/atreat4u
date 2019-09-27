from django.urls import path
<<<<<<< HEAD
from .views import index, about, contact, meal, meal_details, restaurant, comedy, comedy_details, cinemas, cinemas_details, salons, salons_details, music, music_details, delete_celeb,  business, business_details, tvhost, tvhost_details, restaurant_location, meal_location, celeb_test, celeb_test_detail, delete_music, delete_business, delete_tvhost, cinema_location
=======
from .views import index, about, contact, meal, meal_details, restaurant, comedy, comedy_details, cinemas, cinemas_details, salons, salons_details, music, music_details, delete_celeb,  business, business_details, tvhost, tvhost_details, restaurant_location, meal_location, celeb_test, celeb_test_detail, delete_music, delete_business, delete_tvhost, add_meal_cart
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c

app_name = 'catalog'

urlpatterns = [

    path('', index, name='index' ),
    path('about', about, name='about' ),
    path('contact', contact, name='contact' ),
    path('test', celeb_test, name='test' ),
    path('test/<slug:slug>', celeb_test_detail, name='test2' ),
    path('meal', meal, name='meal' ),
    path('location', restaurant, name='location' ),
<<<<<<< HEAD

    path('comedy', comedy, name='comedy' ),
    path('cinemas', cinemas, name='cinemas' ),
    path('cinema_location', cinema_location, name='cinema_location' ),
=======
    path('add_meal_cart/<slug:id>', add_meal_cart, name='add_meal_cart' ),
    path('comedy', comedy, name='comedy' ),
    path('cinemas', cinemas, name='cinemas' ),
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
	#path('cinemas/<slug:slug>', update_cinema, name='update_cinema' ),
    path('salons', salons, name='salons' ),
    path('salon/<slug:slug>', salons_details, name='salons_detail' ),
    path('restaurant/<slug:slug>', meal_details, name='meal_restaurant' ),
    path('restaurant-location/<slug:slug>', restaurant_location, name='restaurant_location' ),

    path('comedy/<slug:slug>', comedy_details, name='comedy_details' ),
	path('cinemas/<slug:slug>', cinemas_details, name='cinemas_details' ),
    path('movie', celeb_test, name='movie' ),
	path('movie/<slug:slug>', celeb_test_detail, name='movie_details' ),
    path('deleteceleb/<slug:slug>', delete_celeb, name='delete_celeb' ),

    path('music', music, name='music' ),
	path('music/<slug:slug>', music_details, name='music_details' ),
    path('deletecmusic/<slug:slug>', delete_music, name='delete_music' ),

    path('business', business, name='business' ),
	path('business/<slug:slug>', business_details, name='business_details' ),
    path('deletebusiness/<slug:slug>', delete_business, name='delete_business' ),

    path('tvhost', tvhost, name='tvhost' ),
	path('tvhost/<slug:slug>', tvhost_details, name='tvhost_details' ),
    path('deletetvhost/<slug:slug>', delete_tvhost, name='delete_tvhost' ),

    path('location/<slug:restaurant>/<slug:slug>', meal_location, name='meal_location' ),

]
