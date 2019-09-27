from django.shortcuts import render, get_object_or_404, redirect
<<<<<<< HEAD
from .models import CinemaData, Restaurants, Location, Meal, Comedy, Cinemas, Salon, CelebrityTest, Cbid, MusicBid, BusinessBid, TvhostBid, CinemasDetail, CinemaLocation, RestaurantData, CinemaData
=======
from .models import Restaurants, Location, Meal, Comedy, Cinemas, Salon, CelebrityTest, Cbid, MusicBid, BusinessBid, TvhostBid, CinemasDetail
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
from .forms import MealForm, CbidForm, MusicBidForm, BusinessBidForm, TvhostBidForm
from cart.forms import CelebBid, CelebRebid
from django.contrib.auth.models import User
from cart.models import CelebrityBid, RebidCeleb, UserMeal, UserCinemas
<<<<<<< HEAD
from urllib.parse import quote, quote_plus
from django.http import HttpResponseRedirect, HttpResponse
from urllib.parse import quote, quote_plus
from django.contrib.auth.decorators import login_required


a=0
total_list = []
def index(request):
	return render(request, 'index1.html', {})
=======

from django.http import HttpResponseRedirect, HttpResponse
a=0
total_list = []
def index(request):
	return render(request, 'index.html', {})
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c

def about(request):
	return render(request, 'about.html', {})

def contact(request):
	return render(request, 'contact.html', {})
def meal(request):
	restaurant = Restaurants.objects.all()
	context = {'restaurant':restaurant}
	return render(request, 'outdoor-meal.html', context)

<<<<<<< HEAD
# def meal_detail(request, slug):


def meal_details(request, slug):
    restaurant = get_object_or_404(Restaurants, id=slug )
    restaurant_loop = Restaurants.objects.filter(id=slug )
# 	restaurant = get_object_or_404(Restaurants, slug=slug )
# 	restaurant_loop = Restaurants.objects.filter(slug=slug )
    restaurant_location = restaurant.restaurant_location.all()
    restaurant_name = Restaurants.objects.all()
# 	meal_order = Meal.objects.filter(real_restaurant=restaurant.name)
 #'meal_order':meal_order,
	# location = Location.objects.filter(Restaurant=restaurant)
    context = {'restaurant':restaurant, 'restaurant_location':restaurant_location, 'restaurant_name':restaurant_name, 'restaurant_loop':restaurant_loop}
    return render(request, 'meal-detail.html', context)


# def restaurant(request):
#     cname = request.POST.get('dropdown1')
#     location = Location.objects.get(address__iexact=cname)
#     location_id = location.id

#     # location = Location.objects.get(address__iexact=cname)
#     meal = Meal.objects.filter(location=location_id, available=True)
#     # meal = Meal.objects.filter(location_slug__iexact=cname)
#     restaurant_name = Restaurants.objects.all()
#     context = {'cname':cname, 'location':location, 'meal':meal, 'restaurant_name':restaurant_name}
#     return render(request, 'meal.html', context)



def restaurant(request):
    cname= request.POST.get('dropdown1')
    location = Location.objects.get(address__iexact=cname)
    location_id = location.id
    current_restaurant = location.Restaurant
    current_restaurant_image1 = Restaurants.objects.get(slug=current_restaurant)
    current_restaurant_image=current_restaurant_image1.image
    det = RestaurantData.objects.get_or_create(id=1)[0]
    det.location=cname
    det.restaurant = current_restaurant_image1.name
    det.save()
    meal = Meal.objects.filter(location=location_id, available=True)
    restaurant_name = Restaurants.objects.all()
    context = {'cname':cname, 'location':location, 'meal':meal, 'restaurant_name':restaurant_name, 'cname':cname, 'current_restaurant':current_restaurant, 'current_restaurant_image':current_restaurant_image}
    return render(request, 'meal.html', context)

=======
# def meal_detail(request, slug): 


def meal_details(request, slug):
	restaurant = get_object_or_404(Restaurants, slug=slug )
	restaurant_loop = Restaurants.objects.filter(slug=slug )
	restaurant_location = restaurant.restaurant_location.all()
	restaurant_name = Restaurants.objects.all()
	meal_order = Meal.objects.filter(real_restaurant=restaurant.name)

	# location = Location.objects.filter(Restaurant=restaurant)
	context = {'restaurant':restaurant, 'restaurant_location':restaurant_location, 'meal_order':meal_order, 'restaurant_name':restaurant_name, 'restaurant_loop':restaurant_loop}
	return render(request, 'meal-detail.html', context)


def restaurant(request):

	cname = request.POST.get('dropdown1')
	# if request.method=='POST':
	location = Location.objects.get(address=cname)
	meal = Meal.objects.filter(location_slug=cname)
	restaurant_name = Restaurants.objects.all()
	# if request.method == 'POST':


	context = {'cname':cname, 'location':location, 'meal':meal, 'restaurant_name':restaurant_name}
	return render(request, 'meal.html', context)


def add_meal_cart(request, id):
	meal = Meal.objects.get(id=id)
	cname = request.POST.get('detail')
	a = get_object_or_404(Meal, pk=id)
	b = UserMeal()
	b.real_restaurant = a.real_restaurant
	b.location = a.location
	b.Menu = a.Menu
	b.Brand = a.Brand
	b.Size = a.Size
	b.quantity = cname
	b.price = a.Amount
	b.Total_price = int(b.price) * int(cname)
	b.user = request.user.username
	b.save()
	return redirect('cart:view_cart')


# def update_cinema(request, id):
# 	detail = get_object_or_404(CinemasDetail, id=id)
# 	cname = request.POST.get('test')
# 	cinemas_form = UserCinemas()
# 	cinemas_form.cinema_name = detail.cinema_name
# 	cinemas_form.movie = detail.movie	
# 	cinemas_form.slug = detail.slug
# 	cinemas_form.image = detail.image
# 	cinemas_form.rating = cname #detail.rating
# 	cinemas_form.price = detail.price
# 	cinemas_form.price = detail.price
# 	cinemas_form.date = detail.date
# 	cinemas_form.time = detail.time
# 	cinemas_form.user=request.user.username
# 	cinemas_form.save()
# 	print(cname)
# 	return redirect('cart:view_cart')
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c


def restaurant_location(request, slug):
	restaurant = get_object_or_404(Restaurants, slug=slug )
	detail = restaurant.objects.filter(real_restaurant=slug)
	context = {'detail':detail}
	return render(request, 'restaurant-location.html', context)
def meal_location(request, restaurant, slug):
	restaurant = get_object_or_404(Restaurants, slug=restaurant)
	location = Meal.objects.filter(real_restaurant=restaurant, location_slug=slug)
	# location = Meal.objects.filter(restaurant=restaurant, location=location)
	context={'restaurant':restaurant, 'location':location}
	return render(request, 'restaurant-location.html', context)


def comedy(request):
	comedy_event = Comedy.objects.all()
	context = {'comedy_event':comedy_event}
	return render(request, 'comedy-events.html', context)



def comedy_details(request, slug):
	detail = get_object_or_404(Comedy, slug=slug)
	detail_id = Comedy.objects.filter(slug=slug)
<<<<<<< HEAD

=======
	
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
	comedy_event = Comedy.objects.all()
	context = {'detail':detail, 'comedy_event':comedy_event, 'detail_id':detail_id}
	return render(request, 'comedy-detail.html', context)


<<<<<<< HEAD
def cinemas(request):
    cinema_name = Cinemas.objects.all()
    context = {'cinema_name':cinema_name}
    return render(request, 'cinemas.html', context)

def cinema_location(request):

    cname= request.POST.get('dropdown1')
    qs = CinemaLocation.objects.get(address=cname)
    detail = CinemasDetail.objects.filter(location=qs.id, available=True)
    det = CinemaLocation.objects.get(address=cname)
    curent_location=det.address
    current_cinema = det.cinema
    current_cinema_image = Cinemas.objects.get(name=det.cinema).image
    cinema_name = Cinemas.objects.all()
    context = {'cname':cname, 'detail':detail, 'cinema_name':cinema_name, 'curent_location':curent_location, 'current_cinema':current_cinema, 'current_cinema_image':current_cinema_image}
    return render(request, 'cinema_location.html', context)

def cinemas_details(request, slug):
    detail = get_object_or_404(Cinemas, slug=slug)
    location = detail.cinema_location.all()
    movie = detail.cinema_name.all()
    cinema_name = Cinemas.objects.all()
    context = {'detail':detail, 'movie':movie, 'cinema_name':cinema_name, 'location':location}
    return render(request, 'cinemas_detail.html', context)

=======

def cinemas(request):
	cinema_name = Cinemas.objects.all()
	context = {'cinema_name':cinema_name}
	return render(request, 'cinemas.html', context)

def cinemas_details(request, slug):
	detail = get_object_or_404(Cinemas, slug=slug)
	movie = detail.cinema_name.all()
	cinema_name = Cinemas.objects.all()
	context = {'detail':detail, 'movie':movie, 'cinema_name':cinema_name}
	return render(request, 'cinemas_detail.html', context)
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c


def salons(request):
	salon_name = Salon.objects.all()
	context = {'salon_name':salon_name}
	return render(request, 'beauty-Salons.html', context)


def salons_details(request, slug):
	salon = get_object_or_404(Salon, slug=slug )
	salon_style = salon.salon_name.all()
	salon_name = Salon.objects.all()
	context = {'salon':salon, 'salon_style':salon_style, 'salon_name':salon_name}
	return render(request, 'salon-detail.html', context)

def celeb_test(request):
	info = CelebrityTest.objects.filter(category='Nollywood Celebrities')
	return render(request, 'movie.html', {'info':info})

def celeb_test_detail(request, slug):
<<<<<<< HEAD

	info = CelebrityTest.objects.filter(category='Nollywood Celebrities')
	name = CelebrityTest.objects.filter(category='Nollywood Celebrities')
	detail2 = get_object_or_404(CelebrityTest, id=slug )
	total_bid = Cbid.objects.filter(celeb=detail2.name).order_by('-amount')[:1]
	share_string = quote_plus(detail2.treat_description)
	try:


		det = Cbid.objects.get(user=request.user.username, celeb=detail2.name)
		result = 'You Bid #' + str(det.new_amount)
		text = 'Rebid'
		if request.method =='POST':
			form=CbidForm(request.POST or None)
			if form.is_valid():
				a=form.cleaned_data.get('amount')
				if det.new_amount > a:
					return HttpResponse('New amount must be greater than old amount')
				else:
					det.amount = a- det.new_amount
					det.paid = False
					det.save()

					return redirect('cart:view_cart')
		else:
			form = CbidForm()

=======
	
	info = CelebrityTest.objects.filter(category='Nollywood Celebrities')
	name = CelebrityTest.objects.filter(category='Nollywood Celebrities')
	detail2 = get_object_or_404(CelebrityTest, slug=slug )
	total_bid = Cbid.objects.filter(celeb=detail2.name).order_by('-amount')[:1]	
	try:
		
			
		det = Cbid.objects.get(user=request.user.username, celeb=detail2.name)
		result = 'You Bid #' + str(det.amount)
		text = 'Rebid'
		if request.method =='POST':		
			form=CbidForm(request.POST or None)
			if form.is_valid():
				a=form.cleaned_data.get('amount')
				if det.amount > a:
					return HttpResponse('New amount must be greater than old amount')
				else:
					det.amount = a - det.amount
					det.save()
					return redirect('cart:view_cart')
		else:
			form = CbidForm()
				
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
		# return HttpResponse('yeah')
	except Cbid.DoesNotExist:
		# total_bid = max(Cbid.objects.all())
		result = "You Haven't Bid"
		text = 'Submit'
		if request.method=='POST':
			form=CbidForm(request.POST or None)
			if form.is_valid():
				a=form.cleaned_data.get('amount')
<<<<<<< HEAD
				det = Cbid.objects.create(user=request.user.username, celeb=detail2.name, amount=a)
				return redirect('cart:view_cart')
		else:
			form = CbidForm()


	return render(request, 'moviedetail.html', {'detail2':detail2, 'name':name, 'form':form, 'info':info, 'text':text, 'result':result, 'total_bid':total_bid, 'share_string':share_string})

@login_required(login_url='/accounts/login/')
=======
				det = Cbid.objects.create(user=request.user.username, celeb=detail2.name, amount='0.00')
				det.amount = a
				det.save()
				return redirect('cart:view_cart')
		else:
			form = CbidForm()
		

	return render(request, 'moviedetail.html', {'detail2':detail2, 'name':name, 'form':form, 'info':info, 'text':text, 'result':result, 'total_bid':total_bid})

>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
def delete_celeb(request, slug):
	detail = get_object_or_404(Cbid, id=slug)
	detail.delete()
	return redirect('cart:view_cart')


def music(request):
	info = CelebrityTest.objects.filter(category='musical Artist Celebrities')
	return render(request, 'music.html', {'info':info})


def music_details(request, slug):
	info = CelebrityTest.objects.filter(category='musical Artist Celebrities')
	name = CelebrityTest.objects.filter(category='musical Artist Celebrities')
<<<<<<< HEAD
	detail2 = get_object_or_404(CelebrityTest, id=slug )
	total_bid = MusicBid.objects.filter(celeb=detail2.name).order_by('-amount')[:1]
	share_string = quote_plus(detail2.treat_description)
	try:
		det = MusicBid.objects.get(user=request.user.username, celeb=detail2.name)
		result = 'You Bid #' + str(det.new_amount)
		text = 'Rebid'
		if request.method =='POST':
			total_bid = MusicBid.objects.filter(celeb=detail2.name).order_by('-amount')[:1]
			form=MusicBidForm(request.POST or None)
			if form.is_valid():
				a=form.cleaned_data.get('amount')
				if det.new_amount > a:
					return HttpResponse('New amount must be greater than old amount')
				else:
					det.amount = a- det.new_amount
					det.paid = False
					det.save()

=======
	detail2 = get_object_or_404(CelebrityTest, slug=slug )
	total_bid = MusicBid.objects.filter(celeb=detail2.name).order_by('-amount')[:1]	
	try:
		det = MusicBid.objects.get(user=request.user.username, celeb=detail2.name)
		result = 'You Bid #' + str(det.amount)
		text = 'Rebid'
		if request.method =='POST':	
			total_bid = MusicBid.objects.filter(celeb=detail2.name).order_by('-amount')[:1]	
			form=MusicBidForm(request.POST or None)
			if form.is_valid():
				a=form.cleaned_data.get('amount')
				if det.amount > a:
					return HttpResponse('New amount must be greater than old amount')
				else:
					det.amount = a- det.amount
					det.save()
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
				return redirect('cart:view_cart')
		else:
			form = form=MusicBidForm()
	except MusicBid.DoesNotExist:

		result = "You Haven't Bid"
		text = 'Submit'
		if request.method=='POST':
			form=MusicBidForm(request.POST or None)
			if form.is_valid():
				a=form.cleaned_data.get('amount')
<<<<<<< HEAD
				det = MusicBid.objects.create(user=request.user.username, celeb=detail2.name, amount=a)
				return redirect('cart:view_cart')
		else:
			form = MusicBidForm()


	return render(request, 'musicdetail.html', {'detail2':detail2, 'name':name, 'form':form, 'info':info, 'text':text, 'result':result, 'total_bid':total_bid, 'share_string':share_string})

@login_required(login_url='/accounts/login/')
=======
				det = MusicBid.objects.create(user=request.user.username, celeb=detail2.name, amount='0.00')
				det.amount = a
				det.save()
				return redirect('cart:view_cart')
		else:
			form = MusicBidForm()
		

	return render(request, 'musicdetail.html', {'detail2':detail2, 'name':name, 'form':form, 'info':info, 'text':text, 'result':result, 'total_bid':total_bid})


>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
def delete_music(request, slug):
	detail = get_object_or_404(MusicBid, id=slug)
	detail.delete()
	return redirect('cart:view_cart')

def business(request):
	info = CelebrityTest.objects.filter(category='Business Icon Celebrities')
	return render(request, 'business.html', {'info':info})


def business_details(request, slug):
	info = CelebrityTest.objects.filter(category='Business Icon Celebrities')
	name = CelebrityTest.objects.filter(category='Business Icon Celebrities')
<<<<<<< HEAD
	detail2 = get_object_or_404(CelebrityTest, id=slug )
	total_bid = BusinessBid.objects.filter(celeb=detail2.name).order_by('-amount')[:1]
	share_string = quote_plus(detail2.treat_description)
	try:
		det = BusinessBid.objects.get(user=request.user.username, celeb=detail2.name)
		result = 'You Bid #' + str(det.new_amount)
		text = 'Rebid'
		if request.method == 'POST':
			form=BusinessBidForm(request.POST or None)
			if form.is_valid():
				a=form.cleaned_data.get('amount')
				if det.new_amount > a:
					return HttpResponse('New amount must be greater than old amount')
				else:
					det.amount = a- det.new_amount
					det.paid = False
=======
	detail2 = get_object_or_404(CelebrityTest, slug=slug )
	total_bid = BusinessBid.objects.filter(celeb=detail2.name).order_by('-amount')[:1]	
	try:
		det = BusinessBid.objects.get(user=request.user.username, celeb=detail2.name)
		result = 'You Bid #' + str(det.amount)
		text = 'Rebid'
		if request.method == 'POST':			
			form=BusinessBidForm(request.POST or None)
			if form.is_valid():
				a=form.cleaned_data.get('amount')
				if det.amount > a:
					return HttpResponse('New amount must be greater than old amount')
				else:
					det.amount = a- det.amount
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
					det.save()
				return redirect('cart:view_cart')
		else:
			form=BusinessBidForm()
	except BusinessBid.DoesNotExist:

		result = "You Haven't Bid"
		text = 'Submit'
		if request.method=='POST':
			form=BusinessBidForm(request.POST or None)
			if form.is_valid():
				a=form.cleaned_data.get('amount')
<<<<<<< HEAD
				det = BusinessBid.objects.create(user=request.user.username, celeb=detail2.name, amount=a)
				return redirect('cart:view_cart')
		else:
			form = BusinessBidForm()


	return render(request, 'businessdetail.html', {'detail2':detail2, 'name':name, 'form':form, 'info':info, 'text':text, 'result':result, 'total_bid':total_bid, 'share_string':share_string})

@login_required(login_url='/accounts/login/')
=======
				det = BusinessBid.objects.create(user=request.user.username, celeb=detail2.name, amount='0.00')
				det.amount = a
				det.save()
				return redirect('cart:view_cart')
		else:
			form = BusinessBidForm()
		

	return render(request, 'businessdetail.html', {'detail2':detail2, 'name':name, 'form':form, 'info':info, 'text':text, 'result':result, 'total_bid':total_bid})

>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
def delete_business(request, slug):
	detail = get_object_or_404(BusinessBid, id=slug)
	detail.delete()
	return redirect('cart:view_cart')

def tvhost(request):

	info = CelebrityTest.objects.filter(category='TV Host Celebrities')
	return render(request, 'tvhost.html', {'info':info})


def tvhost_details(request, slug):
	info = CelebrityTest.objects.filter(category='TV Host Celebrities')
	name = CelebrityTest.objects.filter(category='TV Host Celebrities')
<<<<<<< HEAD
	detail2 = get_object_or_404(CelebrityTest, id=slug )
	total_bid = TvhostBid.objects.filter(celeb=detail2.name).order_by('-amount')[:1]
	share_string = quote_plus(detail2.treat_description)
	try:
		det = TvhostBid.objects.get(user=request.user.username, celeb=detail2.name)
		result = 'You Bid #' + str(det.new_amount)
		text = 'Rebid'
		if request.method == 'POST':
			form=TvhostBidForm(request.POST or None)
			if form.is_valid():
				a=form.cleaned_data.get('amount')
				if det.new_amount > a:
					return HttpResponse('New amount must be greater than old amount')
				else:
					det.amount = a- det.new_amount
					det.paid = False
=======
	detail2 = get_object_or_404(CelebrityTest, slug=slug )
	total_bid = TvhostBid.objects.filter(celeb=detail2.name).order_by('-amount')[:1]	
	try:
		det = TvhostBid.objects.get(user=request.user.username, celeb=detail2.name)
		result = 'You Bid #' + str(det.amount)
		text = 'Rebid'
		if request.method == 'POST':			
			form=TvhostBidForm(request.POST or None)
			if form.is_valid():
				a=form.cleaned_data.get('amount')
				if det.amount > a:
					return HttpResponse('New amount must be greater than old amount')
				else:
					det.amount = a- det.amount
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
					det.save()
				return redirect('cart:view_cart')
		form=TvhostBidForm()
	except TvhostBid.DoesNotExist:

		result = "You Haven't Bid"
		text = 'Submit'
		if request.method=='POST':
			form=TvhostBidForm(request.POST or None)
			if form.is_valid():
				a=form.cleaned_data.get('amount')
<<<<<<< HEAD
				det = TvhostBid.objects.create(user=request.user.username, celeb=detail2.name, amount=a)
				return redirect('cart:view_cart')
		else:
			form = TvhostBidForm()


	return render(request, 'tvhostdetail.html', {'detail2':detail2, 'name':name, 'form':form, 'info':info, 'text':text, 'result':result, 'total_bid':total_bid, 'share_string':share_string})

@login_required(login_url='/accounts/login/')
=======
				det = TvhostBid.objects.create(user=request.user.username, celeb=detail2.name, amount='0.00')
				det.amount = a
				det.save()
				return redirect('cart:view_cart')
		else:
			form = TvhostBidForm()
		

	return render(request, 'tvhostdetail.html', {'detail2':detail2, 'name':name, 'form':form, 'info':info, 'text':text, 'result':result, 'total_bid':total_bid})


>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
def delete_tvhost(request, slug):
	detail = get_object_or_404(TvhostBid, id=slug)
	detail.delete()
	return redirect('cart:view_cart')
