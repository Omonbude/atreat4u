<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from cart.models import MealCart, UserMeal, UserCinemas, UserSalon, UserComedySingle, UserComedyDouble, UserComedyRound, UserComedyVip, CelebrityBid, RebidCeleb
from catalog.models import Meal, Comedy, CinemasDetail, SalonDetail, Cbid, MusicBid, BusinessBid, TvhostBid, LogoImage
from twilio.rest import Client
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from atreat.utils import render_to_pdf
from django.template.loader import get_template


@login_required(login_url='/accounts/login/')
=======
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from cart.models import MealCart, UserMeal, UserCinemas, UserSalon, UserComedySingle, UserComedyDouble, UserComedyRound, UserComedyVip, CelebrityBid, RebidCeleb
from catalog.models import Meal, Comedy, CinemasDetail, SalonDetail, Cbid, MusicBid, BusinessBid, TvhostBid


@login_required(login_url='/accounts/login')
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
def order(request):
	if request.method=='POST':
		form=OrderForm(request.POST or None)
		if form.is_valid():
			a = form.cleaned_data.get('user')
			a = request.user.username
<<<<<<< HEAD
			phone_nummber = form.cleaned_data.get('RecipientPhoneNumber')
			resipient_name = form.cleaned_data.get('RecipientName')
			treat_occasion = form.cleaned_data.get('TreatOccasion')
			return redirect('cart:myproducts')
=======
			# a.save()
			form.save()
			return redirect('order:payment')
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
	else:
		form = OrderForm()
	return render(request, 'order.html', {'form':form})

<<<<<<< HEAD
@login_required(login_url='/accounts/login/')
def generatepdf(request):
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

	celeb_count = Cbid.objects.filter(user=request.user.username, paid=True).count()

	celeb = Cbid.objects.filter(user=request.user.username, paid=True).order_by('-date')

	music_count = MusicBid.objects.filter(user=request.user.username, paid=True).count()
	music = MusicBid.objects.filter(user=request.user.username, paid=True).order_by('-date')

	business_count = BusinessBid.objects.filter(user=request.user.username, paid=True).count()
	business = BusinessBid.objects.filter(user=request.user.username, paid=True).order_by('-date')

	tv_count=TvhostBid.objects.filter(user=request.user.username, paid=True).count()
	tv=TvhostBid.objects.filter(user=request.user.username, paid=True).order_by('-date')
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
	username=request.user.username
	logo = LogoImage.objects.get(id=1)
	template = get_template('pdf.html')
	context = {"logo":logo, "username":username, 'x':x, 'meal_total':meal_total, 'total_items':total_items, 'qs':qs, 'cinema_total':cinema_total, 'total_price':total_price, 'salon_total':salon_total, 'single_total':single_total, 'double_total':double_total, 'round_total':round_total, 'vip_total':vip_total, 'celeb':celeb, 'music':music, 'business':business, 'tv':tv}
	html = template.render(context)
	pdf = render_to_pdf('pdf.html', context)
	if pdf:
		response = HttpResponse(pdf, content_type='application/pdf')

		filename = "%s_receipt.pdf" %('atreat4u')
		content = "inline; filename=%s" %(filename)
		download = request.GET.get("download")
		if download:
			content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response
	return HttpResponse("Not found")






#The following code is to delete query from myproducts...

@login_required(login_url='/accounts/login/')
def delete_mealcart(request, id):
	detail = UserMeal.objects.get(pk=id, paid=True)
	detail.delete()
	return redirect('cart:myproducts')

@login_required(login_url='/accounts/login/')
def delete_comedy_singlecart(request, slug):
	detail = get_object_or_404(UserComedySingle, id=slug, paid=True)
	detail.delete()
	return redirect('cart:myproducts')

@login_required(login_url='/accounts/login/')
def delete_comedy_doublecart(request, slug):
	detail = get_object_or_404(UserComedyDouble, id=slug, paid=True)
	detail.delete()
	return redirect('cart:myproducts')

@login_required(login_url='/accounts/login/')
def delete_comedy_round_tablecart(request, slug):
	detail = get_object_or_404(UserComedyRound, id=slug, paid=True)
	detail.delete()
	return redirect('cart:myproducts')

@login_required(login_url='/accounts/login/')
def delete_comedy_vip_tablecart(request, slug):
	detail = get_object_or_404(UserComedyVip, id=slug, paid=True)
	detail.delete()
	return redirect('cart:myproducts')

@login_required(login_url='/accounts/login/')
def delete_cinemas_cart(request, slug):
	detail = UserCinemas.objects.filter(pk=slug, paid=True)
	detail.delete()
	return redirect('cart:myproducts')

@login_required(login_url='/accounts/login/')
def delete_salon_cart(request, slug):
	detail = UserSalon.objects.filter(pk=slug, paid=True)
	detail.delete()
	return redirect('cart:myproducts')

@login_required(login_url='/accounts/login/')
def delete_celeb(request, slug):
	detail = get_object_or_404(Cbid, id=slug, paid=True)
	detail.delete()
	return redirect('cart:myproducts')

@login_required(login_url='/accounts/login/')
def delete_music(request, slug):
	detail = get_object_or_404(MusicBid, id=slug, paid=True)
	detail.delete()
	return redirect('cart:myproducts')

@login_required(login_url='/accounts/login/')
def delete_business(request, slug):
	detail = get_object_or_404(BusinessBid, id=slug, paid=True)
	detail.delete()
	return redirect('cart:myproducts')

@login_required(login_url='/accounts/login/')
def delete_tvhost(request, slug):
	detail = get_object_or_404(TvhostBid, id=slug, paid=True)
	detail.delete()
	return redirect('cart:myproducts')



def payment(request):
	mealprice_count = UserMeal.objects.filter(user=request.user.username, paid=False).count()
	meal_total = UserMeal.objects.filter(user=request.user.username, paid=False)

	single_count =  UserComedySingle.objects.filter(user=request.user.username, paid=False).count()
	single_total = UserComedySingle.objects.filter(user=request.user.username, paid=False)

	double_count = UserComedyDouble.objects.filter(user=request.user.username, paid=False).count()
	double_total = UserComedyDouble.objects.filter(user=request.user.username, paid=False)

	round_count = UserComedyRound.objects.filter(user=request.user.username, paid=False).count()
	round_total = UserComedyRound.objects.filter(user=request.user.username, paid=False)

	vip_count = UserComedyVip.objects.filter(user=request.user.username, paid=False).count()
	vip_total = UserComedyVip.objects.filter(user=request.user.username, paid=False)

	# cinemaprice_count = UserCinemas.filter(user=request.user.username).count()
	cinemaprice_count = UserCinemas.objects.filter(user=request.user.username, paid=False).count()
	cinema_total = UserCinemas.objects.filter(user=request.user.username, paid=False)

	salonprice_count = UserSalon.objects.filter(user=request.user.username, paid=False).count()
	salon_total = UserSalon.objects.filter(user=request.user.username, paid=False)

	celeb_count = Cbid.objects.filter(user=request.user.username, paid=False).count()

	celeb = Cbid.objects.filter(user=request.user.username, paid=False)

	music_count = MusicBid.objects.filter(user=request.user.username, paid=False).count()
	music = MusicBid.objects.filter(user=request.user.username, paid=False)

	business_count = BusinessBid.objects.filter(user=request.user.username, paid=False).count()
	business = BusinessBid.objects.filter(user=request.user.username, paid=False)

	tv_count=TvhostBid.objects.filter(user=request.user.username, paid=False).count()
	tv=TvhostBid.objects.filter(user=request.user.username, paid=False)
	x=0
	qs=0
	y=0

=======
def payment(request):
	mealprice_count = UserMeal.objects.filter(user=request.user.username).count()
	meal_total = UserMeal.objects.filter(user=request.user.username)

	single_count =  UserComedySingle.objects.filter(user=request.user.username).count()
	single_total = UserComedySingle.objects.filter(user=request.user.username)

	double_count = UserComedyDouble.objects.filter(user=request.user.username).count()
	double_total = UserComedyDouble.objects.filter(user=request.user.username)

	round_count = UserComedyRound.objects.filter(user=request.user.username).count()
	round_total = UserComedyRound.objects.filter(user=request.user.username)

	vip_count = UserComedyVip.objects.filter(user=request.user.username).count()
	vip_total = UserComedyVip.objects.filter(user=request.user.username)

	# cinemaprice_count = UserCinemas.filter(user=request.user.username).count()
	cinemaprice_count = UserCinemas.objects.filter(user=request.user.username).count()
	cinema_total = UserCinemas.objects.filter(user=request.user.username)

	salonprice_count = UserSalon.objects.filter(user=request.user.username).count()
	salon_total = UserSalon.objects.filter(user=request.user.username)

	celeb_count = Cbid.objects.filter(user=request.user.username).count()

	celeb = Cbid.objects.filter(user=request.user.username)

	music_count = MusicBid.objects.filter(user=request.user.username).count()	
	music = MusicBid.objects.filter(user=request.user.username)

	business_count = BusinessBid.objects.filter(user=request.user.username).count()	
	business = BusinessBid.objects.filter(user=request.user.username)

	tv_count=TvhostBid.objects.filter(user=request.user.username).count()	
	tv=TvhostBid.objects.filter(user=request.user.username)
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


	# print(y)
<<<<<<< HEAD
	total_price = x + qs + y + a + b + c + d + e + f + g + h + 100
	total_items = mealprice_count + cinemaprice_count + salonprice_count + single_count + double_count + round_count + vip_count + celeb_count + music_count + business_count + tv_count
	return render(request, 'payment.html', {'x':x, 'meal_total':meal_total, 'total_items':total_items, 'qs':qs, 'cinema_total':cinema_total, 'total_price':total_price, 'salon_total':salon_total, 'single_total':single_total, 'double_total':double_total, 'round_total':round_total, 'vip_total':vip_total, 'celeb':celeb, 'music':music, 'business':business, 'tv':tv })





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

	celeb_count = Cbid.objects.filter(user=request.user.username, paid=True).count()

	celeb = Cbid.objects.filter(user=request.user.username, paid=True).order_by('-date')

	music_count = MusicBid.objects.filter(user=request.user.username, paid=True).count()
	music = MusicBid.objects.filter(user=request.user.username, paid=True).order_by('-date')

	business_count = BusinessBid.objects.filter(user=request.user.username, paid=True).count()
	business = BusinessBid.objects.filter(user=request.user.username, paid=True).order_by('-date')

	tv_count=TvhostBid.objects.filter(user=request.user.username, paid=True).count()
	tv=TvhostBid.objects.filter(user=request.user.username, paid=True).order_by('-date')
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
	total_price = x + qs + y + a + b + c + d + e + f + g + h
	total_items = mealprice_count + cinemaprice_count + salonprice_count + single_count + double_count + round_count + vip_count + celeb_count + music_count + business_count + tv_count
	return render(request, 'payment.html', {'x':x, 'meal_total':meal_total, 'total_items':total_items, 'qs':qs, 'cinema_total':cinema_total, 'total_price':total_price, 'salon_total':salon_total, 'single_total':single_total, 'double_total':double_total, 'round_total':round_total, 'vip_total':vip_total, 'celeb':celeb, 'music':music, 'business':business, 'tv':tv })
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
