from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from .forms import CelebBid, CelebRebid, MealQuantityForm
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from .models import MealCart, UserMeal, UserCinemas, UserSalon, UserComedySingle, UserComedyDouble, UserComedyRound, UserComedyVip, CelebrityBid, RebidCeleb

from catalog.models import Meal, Comedy, CinemasDetail, SalonDetail, Cbid, MusicBid, BusinessBid, TvhostBid, RestaurantData
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required



@login_required(login_url='/accounts/login/')
def view_cart(request):
	mealprice_count = UserMeal.objects.filter(user=request.user.username, paid=False).count()
	meal_total = UserMeal.objects.filter(user=request.user.username, paid=False).order_by('-date')

	single_count =  UserComedySingle.objects.filter(user=request.user.username, paid=False).count()
	single_total = UserComedySingle.objects.filter(user=request.user.username, paid=False).order_by('-date')

	double_count = UserComedyDouble.objects.filter(user=request.user.username, paid=False).count()
	double_total = UserComedyDouble.objects.filter(user=request.user.username, paid=False).order_by('-date')

	round_count = UserComedyRound.objects.filter(user=request.user.username, paid=False).count()
	round_total = UserComedyRound.objects.filter(user=request.user.username, paid=False).order_by('-date')

	vip_count = UserComedyVip.objects.filter(user=request.user.username, paid=False).count()
	vip_total = UserComedyVip.objects.filter(user=request.user.username, paid=False).order_by('-date')

	cinemaprice_count = UserCinemas.objects.filter(user=request.user.username, paid=False).count()
	cinema_total = UserCinemas.objects.filter(user=request.user.username, paid=False).order_by('-date')

	salonprice_count = UserSalon.objects.filter(user=request.user.username, paid=False).count()
	salon_total = UserSalon.objects.filter(user=request.user.username, paid=False).order_by('-date')

	celeb_count = Cbid.objects.filter(user=request.user.username, paid=False).count()

	celeb = Cbid.objects.filter(user=request.user.username, paid=False).order_by('-date')

	music_count = MusicBid.objects.filter(user=request.user.username, paid=False).count()
	music = MusicBid.objects.filter(user=request.user.username, paid=False).order_by('-date')

	business_count = BusinessBid.objects.filter(user=request.user.username, paid=False).count()
	business = BusinessBid.objects.filter(user=request.user.username, paid=False).order_by('-date')

	tv_count=TvhostBid.objects.filter(user=request.user.username, paid=False).count()
	tv=TvhostBid.objects.filter(user=request.user.username, paid=False).order_by('-date')
	x=0
	qs=0
	y=0

=======
# from django.views.decorators.http import require_POST
from .models import MealCart, UserMeal, UserCinemas, UserSalon, UserComedySingle, UserComedyDouble, UserComedyRound, UserComedyVip, CelebrityBid, RebidCeleb

from catalog.models import Meal, Comedy, CinemasDetail, SalonDetail, Cbid, MusicBid, BusinessBid, TvhostBid
from django.http import HttpResponseRedirect, HttpResponse
# timezone.now()
# from .cart import Cart
# from .forms import CartAddProductForm
# from django.contrib.auth.models import User
# from django.http import HttpResponse 



def view_cart(request):
	mealprice_count = UserMeal.objects.filter(user=request.user.username).count()
	meal_total = UserMeal.objects.filter(user=request.user.username).order_by('-date')

	single_count =  UserComedySingle.objects.filter(user=request.user.username).count()
	single_total = UserComedySingle.objects.filter(user=request.user.username).order_by('-date')

	double_count = UserComedyDouble.objects.filter(user=request.user.username).count()
	double_total = UserComedyDouble.objects.filter(user=request.user.username).order_by('-date')

	round_count = UserComedyRound.objects.filter(user=request.user.username).count()
	round_total = UserComedyRound.objects.filter(user=request.user.username).order_by('-date')

	vip_count = UserComedyVip.objects.filter(user=request.user.username).count()
	vip_total = UserComedyVip.objects.filter(user=request.user.username).order_by('-date')

	# cinemaprice_count = UserCinemas.filter(user=request.user.username).count()
	cinemaprice_count = UserCinemas.objects.filter(user=request.user.username).count()
	cinema_total = UserCinemas.objects.filter(user=request.user.username).order_by('-date')

	salonprice_count = UserSalon.objects.filter(user=request.user.username).count()
	salon_total = UserSalon.objects.filter(user=request.user.username).order_by('-date')

	celeb_count = Cbid.objects.filter(user=request.user.username).count()

	celeb = Cbid.objects.filter(user=request.user.username).order_by('-date')

	music_count = MusicBid.objects.filter(user=request.user.username).count()	
	music = MusicBid.objects.filter(user=request.user.username).order_by('-date')

	business_count = BusinessBid.objects.filter(user=request.user.username).count()	
	business = BusinessBid.objects.filter(user=request.user.username).order_by('-date')

	tv_count=TvhostBid.objects.filter(user=request.user.username).count()	
	tv=TvhostBid.objects.filter(user=request.user.username).order_by('-date')
	x=0
	qs=0
	y=0
	
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
	a=0
	b=0
	c=0
	d=0
	e=0
	f=0
	g=0
	h=0

<<<<<<< HEAD

=======
	
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
	for i in meal_total:
		x+=(int(i.price))
	for i in cinema_total:
		qs+=(int(i.price))
	for i in salon_total:
		y+=(int(i.price))
	for i in single_total:
		a+=(int(i.singles_price))
	for i in double_total:
		b+=(int(i.double_price))
	for i in round_total:
		c+=(int(i.round_table_price))
	for i in vip_total:
		d+=(int(i.vip_table_price))
	for i in celeb:
		e+=(int(i.amount))
	for i in music:
			f+=(int(i.amount))
	for i in business:
			g+=(int(i.amount))
	for i in tv:
			h+=(int(i.amount))
<<<<<<< HEAD
	total_price = x + qs + y + a + b + c + d + e + f + g + h
	flat_charge = total_price + 100
	total_items = mealprice_count + cinemaprice_count + salonprice_count + single_count + double_count + round_count + vip_count + celeb_count + music_count + business_count + tv_count
	return render(request, 'cart-detail.html', {'flat_charge':flat_charge, 'x':x, 'meal_total':meal_total, 'total_items':total_items, 'qs':qs, 'cinema_total':cinema_total, 'total_price':total_price, 'salon_total':salon_total, 'single_total':single_total, 'double_total':double_total, 'round_total':round_total, 'vip_total':vip_total, 'celeb':celeb, 'music':music, 'business':business, 'tv':tv})







@login_required(login_url='/accounts/login/')
def add_meal_cart(request):
	qs = request.POST.getlist("meal")
	for i in qs:
		startmeal = i.find('startmeal')+9
		endmeal = i.find('endmeal')
		Menu = i[startmeal:endmeal]

		startbrand = i.find("startbrand")+10
		endbrand = i.find("endbrand")
		Brand = i[startbrand:endbrand]

		startsize = i.find("startsize")+9
		endsize = i.find("endsize")
		Size = i[startsize:endsize]


		startamount = i.find("startamount")+11
		endamount = i.find("endamount")
		price = i[startamount:endamount]

		startrestaurant = i.find("startrestaurant")+15
		endrestaurant = i.find("endrestaurant")
		restaurant = i[startrestaurant:endrestaurant]

		startlocation = i.find("startlocation")+13
		endlocation = i.find("endlocation")
		location = i[startlocation:endlocation]

		UserMeal.objects.create(real_restaurant=restaurant, location=location, Menu=Menu, Brand=Brand, Size=Size, price=price, user=request.user.username, Total_price=price, paid=False)
	return redirect('cart:view_cart')


@login_required(login_url='/accounts/login/')
def delete_mealcart(request, id):
	detail = UserMeal.objects.filter(pk=id)
=======


	# print(y)
	total_price = x + qs + y + a + b + c + d + e + f + g + h
	total_items = mealprice_count + cinemaprice_count + salonprice_count + single_count + double_count + round_count + vip_count + celeb_count + music_count + business_count + tv_count
	return render(request, 'cart-detail.html', {'x':x, 'meal_total':meal_total, 'total_items':total_items, 'qs':qs, 'cinema_total':cinema_total, 'total_price':total_price, 'salon_total':salon_total, 'single_total':single_total, 'double_total':double_total, 'round_total':round_total, 'vip_total':vip_total, 'celeb':celeb, 'music':music, 'business':business, 'tv':tv})

 


@login_required(login_url='/accounts/login')
def meal_cart(request, slug):
	meal = Meal.objects.get(id=slug)
	cname = request.POST.get('detail')
	a = get_object_or_404(Meal, pk=slug)
	b = UserMeal()
	b.real_restaurant = a.real_restaurant
	b.location = a.location
	b.Menu = a.Menu
	b.Brand = cname
	b.Size = cname
	b.price = a.Amount
	b.user = request.user.username
	b.save()
	return redirect('cart:view_cart')


def delete_cart(request, slug):
	detail = UserMeal.objects.filter(pk=slug)
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
	detail.delete()
	return redirect('cart:view_cart')


<<<<<<< HEAD



@login_required(login_url='/accounts/login/')
=======
@login_required(login_url='/accounts/login')
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
def comedy_singlecart(request, slug):
	detail = get_object_or_404(Comedy, pk=slug)
	new = UserComedySingle()
	new.name = detail.name
	new.slug = detail.slug
	new.image = detail.image
	new.date = detail.date
	new.time = detail.time
	new.venue = detail.venue
	new.singles_price = detail.singles_price
	new.category = 'singles'
	new.user = request.user.username
	new.save()
	return redirect('cart:view_cart')

<<<<<<< HEAD
@login_required(login_url='/accounts/login/')
=======

>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
def delete_comedy_singlecart(request, slug):
	detail = get_object_or_404(UserComedySingle, id=slug)
	detail.delete()
	return redirect('cart:view_cart')

<<<<<<< HEAD
@login_required(login_url='/accounts/login/')
=======
@login_required(login_url='/accounts/login')
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
def comedy_doublecart(request, slug):
	detail = get_object_or_404(Comedy, pk=slug)
	new = UserComedyDouble()
	new.name = detail.name
	new.slug = detail.slug
	new.image = detail.image
	new.date = detail.date
	new.time = detail.time
	new.venue = detail.venue
	new.double_price = detail.double_price
	new.category = 'double'
	new.user = request.user.username
	new.save()
<<<<<<< HEAD
	return redirect('cart:view_cart')


@login_required(login_url='/accounts/login/')
=======
	# print(detail.double_price)
	# print(detail.slug)
	return redirect('cart:view_cart')


>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
def delete_comedy_doublecart(request, slug):
	detail = get_object_or_404(UserComedyDouble, id=slug)
	detail.delete()
	return redirect('cart:view_cart')


<<<<<<< HEAD
@login_required(login_url='/accounts/login/')
=======
@login_required(login_url='/accounts/login')
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
def comedy_round_tablecart(request, slug):
	detail = get_object_or_404(Comedy, pk=slug)
	new = UserComedyRound()
	new.name = detail.name
	new.slug = detail.slug
	new.image = detail.image
	new.date = detail.date
	new.time = detail.time
	new.venue = detail.venue
	new.round_table_price = detail.round_table_price
	new.category = 'Round Table'
	new.user = request.user.username
	new.save()
<<<<<<< HEAD
	return redirect('cart:view_cart')

@login_required(login_url='/accounts/login/')
=======
		# print(detail)
	# print(detail.slug)
	return redirect('cart:view_cart')

>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
def delete_comedy_round_tablecart(request, slug):
	detail = get_object_or_404(UserComedyRound, id=slug)
	detail.delete()
	return redirect('cart:view_cart')

<<<<<<< HEAD
@login_required(login_url='/accounts/login/')
=======
@login_required(login_url='/accounts/login')
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
def comedy_vip_tablecart(request, slug):
	detail = get_object_or_404(Comedy, pk=slug)
	new = UserComedyVip()
	new.name = detail.name
	new.slug = detail.slug
	new.image = detail.image
	new.date = detail.date
	new.time = detail.time
	new.venue = detail.venue
	new.vip_table_price = detail.vip_table_price
	new.category = 'Vip Table'
	new.user = request.user.username
	new.save()
<<<<<<< HEAD
	return redirect('cart:view_cart')

@login_required(login_url='/accounts/login/')
=======
	# print(detail)
	# print(detail.slug)
	return redirect('cart:view_cart')

>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
def delete_comedy_vip_tablecart(request, slug):
	detail = get_object_or_404(UserComedyVip, id=slug)
	detail.delete()
	return redirect('cart:view_cart')


<<<<<<< HEAD
@login_required(login_url='/accounts/login/')
=======
@login_required(login_url='/accounts/login')
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
def cinemas_cart(request, slug):
	detail = get_object_or_404(CinemasDetail, pk=slug)
	cinemas_form = UserCinemas()
	cinemas_form.cinema_name = detail.cinema_name
<<<<<<< HEAD
	cinemas_form.location = detail.location

	cinemas_form.movie = detail.movie
=======
	cinemas_form.movie = detail.movie	
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
	cinemas_form.slug = detail.slug
	cinemas_form.image = detail.image
	cinemas_form.rating = detail.rating
	cinemas_form.price = detail.price
	cinemas_form.price = detail.price
	cinemas_form.date = detail.date
	cinemas_form.time = detail.time
	cinemas_form.user=request.user.username
	cinemas_form.save()
<<<<<<< HEAD
	return redirect('cart:view_cart')

@login_required(login_url='/accounts/login/')
=======
	# print(detail)
	return redirect('cart:view_cart')
	# cinemas_form.date
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
def delete_cinemas_cart(request, slug):
	detail = UserCinemas.objects.filter(pk=slug)
	detail.delete()
	return redirect('cart:view_cart')

<<<<<<< HEAD
@login_required(login_url='/accounts/login/')
=======
@login_required(login_url='/accounts/login')
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
def salon_cart(request, slug):
	detail = get_object_or_404(SalonDetail, pk=slug)
	salon_form = UserSalon()
	salon_form.name = detail.name
	salon_form.slug = detail.slug
	salon_form.style = detail.style
	salon_form.image = detail.image
	salon_form.gender = detail.gender
	salon_form.price = detail.price
	salon_form.user = request.user.username
	salon_form.save()
	return redirect('cart:view_cart')

<<<<<<< HEAD
@login_required(login_url='/accounts/login/')
=======
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
def delete_salon_cart(request, slug):
	detail = UserSalon.objects.filter(pk=slug)
	detail.delete()
	return redirect('cart:view_cart')

<<<<<<< HEAD
def celebcart(request):
	detail = get_object_or_404(Cbid, pk=slug)

@login_required(login_url='/accounts/login/')
=======
# def rebid_celeb(request):
# 	if request.method=='POST':
# 		form = CelebRebid(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			# detail = RebidCeleb.objects.get(id=1)
# 			# detail.amount = form.amount
# 			# detail.save()
# 			# print(detail.amount)
# 	else:
# 		form = CelebRebid()
# 		context = {'form':form}
# 	return render(request, "rough.html", context)
def celebcart(request):
	detail = get_object_or_404(Cbid, pk=slug)

>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
def rebid_celeb(request):

	try:
		detail = RebidCeleb.objects.get(user=request.user.username)
<<<<<<< HEAD


=======
		
		
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
		if request.method == 'POST':
			form = CelebRebid(request.POST or None)
			if form.is_valid():

				amount  = form.cleaned_data.get("amount")
				if detail.amount>=amount:
					return HttpResponse('New Amount Must Be Greater Than Old Amount')

				else:

					total_amount = amount-detail.amount
					detail.amount=total_amount
					detail.save()
<<<<<<< HEAD
=======
					print(detail.amount)
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
				return redirect('cart:test')

		else:
			form = CelebRebid(request.POST or None)

	except RebidCeleb.DoesNotExist:
		detail = RebidCeleb.objects.create(user=request.user.username, amount=0.00)
<<<<<<< HEAD
=======
		print(detail.amount)
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
		if request.method == 'POST':
			form = CelebRebid(request.POST or None)
			if form.is_valid():
				amount  = form.cleaned_data.get("amount")
<<<<<<< HEAD
=======
				print(amount)
				print(detail.amount)
				print(total_amount)
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
				return redirect('cart:test')

		else:
			form = CelebRebid(request.POST or None)
	if detail.amount == 0.00:
		text='Submit Bid'
	else:
		text='Re-Bid'
		text2 = 'You bidded' + " " + str(detail.amount)
	context = {"form": form, 'detail':detail, 'text':text}
	return render(request, "rough.html", context)
<<<<<<< HEAD

@login_required(login_url='/accounts/login/')
def checkout(request):
    meal_total = UserMeal.objects.filter(user=request.user.username, paid=False)
    single_total = UserComedySingle.objects.filter(user=request.user.username, paid=False)
    double_total = UserComedyDouble.objects.filter(user=request.user.username, paid=False)
    round_total = UserComedyRound.objects.filter(user=request.user.username, paid=False)
    vip_total = UserComedyVip.objects.filter(user=request.user.username, paid=False)
    cinema_total = UserCinemas.objects.filter(user=request.user.username, paid=False)
    salon_total = UserSalon.objects.filter(user=request.user.username, paid=False)
    celeb = Cbid.objects.filter(user=request.user.username, paid=False)
    music = MusicBid.objects.filter(user=request.user.username, paid=False)
    business = BusinessBid.objects.filter(user=request.user.username, paid=False)
    tv=TvhostBid.objects.filter(user=request.user.username, paid=False)

    if meal_total.exists():
        for i in meal_total:
            i.paid=True
            i.date = timezone.now()
            i.save()

    if single_total.exists():
        for i in single_total:
            i.paid=True
            i.date = timezone.now()
            i.save()

    if double_total.exists():
        for i in double_total:
            i.paid=True
            i.date = timezone.now()
            i.save()

    if round_total.exists():
        for i in round_total:
            i.paid=True
            i.date = timezone.now()
            i.save()

    if vip_total.exists():
        for i in vip_total:
            i.paid=True
            i.date = timezone.now()
            i.save()

    if cinema_total.exists():
        for i in cinema_total:
            i.paid=True
            i.date = timezone.now()
            i.save()

    if salon_total.exists():
        for i in salon_total:
            i.paid=True
            i.date = timezone.now()
            i.save()

    if celeb.exists():
        for i in celeb:
            i.paid=True
            i.new_amount_paid = True
            i.new_amount = i.amount + i.new_amount
            i.date = timezone.now()
            i.save()

    if music.exists():
        for i in music:
            i.paid=True
            i.new_amount_paid = True
            i.new_amount = i.amount + i.new_amount
            i.date = timezone.now()
            i.save()

    if business.exists():
        for i in business:
            i.paid=True
            i.new_amount_paid = True
            i.new_amount = i.amount + i.new_amount
            i.date = timezone.now()
            i.save()

    if tv.exists():
        for i in tv:
            i.paid=True
            i.new_amount_paid = True
            i.new_amount = i.amount + i.new_amount
            i.date = timezone.now()
            i.save()


    return redirect('order:index')


@login_required(login_url='/accounts/login/')
def myproducts(request):
	mealprice_count = UserMeal.objects.filter(user=request.user.username, paid=True).count()
	meal_total = UserMeal.objects.filter(user=request.user.username, paid=True).order_by('-date')

	single_count =  UserComedySingle.objects.filter(user=request.user.username, paid=True).count()
	single_total = UserComedySingle.objects.filter(user=request.user.username, paid=True).order_by('-date')

	double_count = UserComedyDouble.objects.filter(user=request.user.username, paid=True).count()
	double_total = UserComedyDouble.objects.filter(user=request.user.username, paid=True).order_by('-date')

	round_count = UserComedyRound.objects.filter(user=request.user.username, paid=True).count()
	round_total = UserComedyRound.objects.filter(user=request.user.username, paid=True).order_by('-date')

	vip_count = UserComedyVip.objects.filter(user=request.user.username, paid=True).count()
	vip_total = UserComedyVip.objects.filter(user=request.user.username, paid=True).order_by('-date')

	cinemaprice_count = UserCinemas.objects.filter(user=request.user.username, paid=True).count()
	cinema_total = UserCinemas.objects.filter(user=request.user.username, paid=True).order_by('-date')

	salonprice_count = UserSalon.objects.filter(user=request.user.username, paid=True).count()
	salon_total = UserSalon.objects.filter(user=request.user.username, paid=True).order_by('-date')

	celeb_count = Cbid.objects.filter(user=request.user.username, new_amount_paid=True).count()

	celeb = Cbid.objects.filter(user=request.user.username, new_amount_paid=True).order_by('-date')

	music_count = MusicBid.objects.filter(user=request.user.username, new_amount_paid=True).count()
	music = MusicBid.objects.filter(user=request.user.username, new_amount_paid=True).order_by('-date')

	business_count = BusinessBid.objects.filter(user=request.user.username, new_amount_paid=True).count()
	business = BusinessBid.objects.filter(user=request.user.username, new_amount_paid=True).order_by('-date')

	tv_count=TvhostBid.objects.filter(user=request.user.username, new_amount_paid=True).count()
	tv=TvhostBid.objects.filter(user=request.user.username, new_amount_paid=True).order_by('-date')
	x=0
	qs=0
	y=0

	a=0
	b=0
	c=0
	d=0
	e=0
	f=0
	g=0
	h=0


	for i in meal_total:
		x+=(int(i.price))
	for i in cinema_total:
		qs+=(int(i.price))
	for i in salon_total:
		y+=(int(i.price))
	for i in single_total:
		a+=(int(i.singles_price))
	for i in double_total:
		b+=(int(i.double_price))
	for i in round_total:
		c+=(int(i.round_table_price))
	for i in vip_total:
		d+=(int(i.vip_table_price))
	for i in celeb:
		e+=(int(i.amount))
	for i in music:
			f+=(int(i.amount))
	for i in business:
			g+=(int(i.amount))
	for i in tv:
			h+=(int(i.amount))

	total_price = x + qs + y + a + b + c + d + e + f + g + h
	total_items = mealprice_count + cinemaprice_count + salonprice_count + single_count + double_count + round_count + vip_count + celeb_count + music_count + business_count + tv_count
	return render(request, 'myproducts.html', {'x':x, 'meal_total':meal_total, 'total_items':total_items, 'qs':qs, 'cinema_total':cinema_total, 'total_price':total_price, 'salon_total':salon_total, 'single_total':single_total, 'double_total':double_total, 'round_total':round_total, 'vip_total':vip_total, 'celeb':celeb, 'music':music, 'business':business, 'tv':tv})
=======
# def comedybid(request):
# 	if request.method == 'POST':
# 		form = CelebBid(request.POST or None)
		
# 		if form.is_valid():
# 			form.save()
# 	else:
# 		form = CelebBid(request.POST or None)
# 	context = {"form": form}
# 	return render(request, "rough.html", context)
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
