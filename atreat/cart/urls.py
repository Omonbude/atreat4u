from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'cart'


<<<<<<< HEAD
urlpatterns = [
    path('test', views.rebid_celeb, name='test'),
    path('', views.view_cart, name='view_cart'),
    path('meal', views.add_meal_cart, name='add_meal_cart'),
    path('delete_meal/<slug:id>', views.delete_mealcart, name='delete_mealcart'),
    path('add_comedy_single/<slug:slug>', views.comedy_singlecart, name='comedy_singlecart'),
    path('delete_comedy_single/<slug:slug>', views.delete_comedy_singlecart, name='delete_comedy_singlecart'),

    path('add_comedy_double/<slug:slug>', views.comedy_doublecart, name='comedy_doublecart'),
    path('delete_comedy_double/<slug:slug>', views.delete_comedy_doublecart, name='delete_comedy_doublecart'),

    path('add_comedy_round_table/<slug:slug>', views.comedy_round_tablecart, name='comedy_round_tablecart'),
    path('delete_comedy_round_table/<slug:slug>', views.delete_comedy_round_tablecart, name='delete_comedy_round_tablecart'),

    path('add_comedy_vip_table/<slug:slug>', views.comedy_vip_tablecart, name='comedy_vip_tablecart'),
    path('delete_comedy_vip_table/<slug:slug>', views.delete_comedy_vip_tablecart, name='delete_comedy_vip_tablecart'),

    path('add_cinema/<slug:slug>', views.cinemas_cart, name='cinema_cart'),
    path('delete_cinema/<slug:slug>', views.delete_cinemas_cart, name='delete_cinemascart'),
    path('add_salon/<slug:slug>', views.salon_cart, name='salon_cart'),
    path('delete_salon/<slug:slug>', views.delete_salon_cart, name='delete_salon_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('myproducts/', views.myproducts, name='myproducts'),
=======
urlpatterns = [ 
	path('test', views.rebid_celeb, name='test'),
	path('', views.view_cart, name='view_cart'),
	path('<slug:slug>', views.meal_cart, name='my_cart'),
	path('delete_meal/<slug:slug>', views.delete_cart, name='delete_mealcart'),
	path('add_comedy_single/<slug:slug>', views.comedy_singlecart, name='comedy_singlecart'),
	path('delete_comedy_single/<slug:slug>', views.delete_comedy_singlecart, name='delete_comedy_singlecart'),

	path('add_comedy_double/<slug:slug>', views.comedy_doublecart, name='comedy_doublecart'),
	path('delete_comedy_double/<slug:slug>', views.delete_comedy_doublecart, name='delete_comedy_doublecart'),

	path('add_comedy_round_table/<slug:slug>', views.comedy_round_tablecart, name='comedy_round_tablecart'),
	path('delete_comedy_round_table/<slug:slug>', views.delete_comedy_round_tablecart, name='delete_comedy_round_tablecart'),

	path('add_comedy_vip_table/<slug:slug>', views.comedy_vip_tablecart, name='comedy_vip_tablecart'),
	path('delete_comedy_vip_table/<slug:slug>', views.delete_comedy_vip_tablecart, name='delete_comedy_vip_tablecart'),

	path('add_cinema/<slug:slug>', views.cinemas_cart, name='cinema_cart'),
	path('delete_cinema/<slug:slug>', views.delete_cinemas_cart, name='delete_cinemascart'),
	path('add_salon/<slug:slug>', views.salon_cart, name='salon_cart'),
	path('delete_salon/<slug:slug>', views.delete_salon_cart, name='delete_salon_cart'),
	

    # path('<slug:>', views.meal_add, name='meal_add'),
 #    path('add/<slug:real_restaurant>', views.cart_add, name='cart_add'),
	# path('remove<slug:real_restaurant>/',views.cart_remove, name='cart_remove'),

>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c


]
