from django.urls import path
from .views import order, payment
<<<<<<< HEAD
from . import views
=======
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c

app_name = 'order'

urlpatterns = [
    path('', order, name='index' ),
<<<<<<< HEAD

    path('payment', payment, name='payment' ),

    path('generatepdf', views.generatepdf, name='generatepdf' ),

    path('delete_meal/<slug:id>', views.delete_mealcart, name='delete_mealcart'),

    path('delete_comedy_single/<slug:slug>', views.delete_comedy_singlecart, name='delete_comedy_singlecart'),


    path('delete_comedy_double/<slug:slug>', views.delete_comedy_doublecart, name='delete_comedy_doublecart'),


    path('delete_comedy_round_table/<slug:slug>', views.delete_comedy_round_tablecart, name='delete_comedy_round_tablecart'),


    path('delete_comedy_vip_table/<slug:slug>', views.delete_comedy_vip_tablecart, name='delete_comedy_vip_tablecart'),


    path('delete_cinema/<slug:slug>', views.delete_cinemas_cart, name='delete_cinemascart'),

    path('delete_salon/<slug:slug>', views.delete_salon_cart, name='delete_salon_cart'),

    path('delete_business/<slug:slug>', views.delete_business, name='delete_business'),

    path('delete_tvhost/<slug:slug>', views.delete_tvhost, name='delete_tvhost'),

    path('delete_music/<slug:slug>', views.delete_music, name='delete_music'),

    path('delete_celeb/<slug:slug>', views.delete_celeb, name='delete_celeb'),



=======
	path('payment', payment, name='payment' ),
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c

    ]