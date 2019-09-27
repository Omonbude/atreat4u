from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
# from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
<<<<<<< HEAD
from .forms import RegisterForm, LoginForm, EmailPasswordReset, ChangePasswordCodeForm, ChangePasswordForm, CreateProfieForm1
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from .models import ChangePasswordCode, CreateProfie
from django.conf import settings
from django.core.mail import send_mail
=======
from .forms import RegisterForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c

# from .forms import test

# User = get_user_model()

def register(request):
	if request.method == 'POST':
<<<<<<< HEAD
		# form = CreateProfieForm1(request.POST or None)
		form = RegisterForm(request.POST or None, request.FILES or None)


=======
		form = RegisterForm(request.POST or None)
		
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
		if form.is_valid():
			username  = form.cleaned_data.get("username")
			email  = form.cleaned_data.get("email")
			password  = form.cleaned_data.get("password")
<<<<<<< HEAD
			first_name  = form.cleaned_data.get("first_name")
			last_name  = form.cleaned_data.get("last_name")
			phone_number  = form.cleaned_data.get("phone_number")
# 			image  = form.cleaned_data.get("image")


			new_user  = User.objects.create_user(username, email, password)
			CreateProfie.objects.create(user=username, email=email, phone=phone_number, first_name=first_name, last_name=last_name)
			return redirect('account:registration_success')

	else:
		form = RegisterForm(request.POST or None)
	context = {"form": form}
	return render(request, "account/register.html", context)

@login_required(login_url='/accounts/login/')
def edit_profile(request):

	# print(request.method)
	try:
		# form=''
		detail=''
		# if request.method == 'GET':
		detail = CreateProfie.objects.get(user=request.user.username)
		form = CreateProfieForm1(request.POST or None, request.FILES or None, instance = detail)
		if form.is_valid():
			form.save()
			return redirect('account:profile')

	except CreateProfie.DoesNotExist :

		# if request.method == 'GET':
		form = CreateProfieForm1(request.POST or None, request.FILES or None)
		if form.is_valid():
			first_name  = form.cleaned_data.get("first_name")
			last_name  = form.cleaned_data.get("last_name")
			phone  = form.cleaned_data.get("phone")
			CreateProfie.objects.create(user=request.user.username, phone=phone, first_name=first_name, last_name=last_name)
			return redirect('account:profile')

	return render(request, 'account/edit_profile.html', {'form':form, 'detail':detail})



@login_required(login_url='/accounts/login/')
def profile(request):
	try:

		qs = CreateProfie.objects.get(user=request.user.username)
	# if qs.exists():
		username = qs.user
		first_name = qs.first_name
		last_name = qs.last_name
		email = qs.email
		phone_number = qs.phone

	except CreateProfie.DoesNotExist :
	# else:
		username = ''
		first_name = ''
		last_name = ''
		email = ''
		phone_number = ''

	context={'username':username, 'first_name':first_name, 'last_name':last_name, 'email':email, 'phone_number':phone_number}
	return render(request, 'account/profile.html', context)





def registration_success(request):
	return render(request, 'account/registration_success.html', {})


=======
			new_user  = User.objects.create_user(username, email, password)
			return redirect('account:login')

	else:
		form = RegisterForm(request.POST or None) 
	context = {"form": form}
	return render(request, "account/register.html", context)




>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
def login_page(request):
	if request.method == 'POST':
		form = LoginForm(request.POST or None)
		if form.is_valid():
			username  = form.cleaned_data.get("username")
			password  = form.cleaned_data.get("password")
			user = authenticate(username=username, password=password)
			if user is not None:
			 	if user.is_active:
			 		login(request, user)
			 		return redirect('/')
			 	else:
			 		return HttpResponse('Disabled account')
			else:
				return HttpResponse('Invalid login')
	else:
		form = LoginForm()
	context = {"form": form}
	return render(request, "account/login.html", context)


def logout_page(request):
<<<<<<< HEAD
	logout(request)
	return redirect('account:logged_out')

def logged_out(request):
	return render(request, "account/logout.html", {})


def reset_password(request):
	if request.method == 'POST':
		form = EmailPasswordReset(request.POST)
		if form.is_valid():

			email = form.cleaned_data.get('email')
			allchar = string.ascii_letters + string.digits
			password = ''.join(choice(allchar) for x in range(13))
			u = User.objects.get(email=email)
			# u.set_password(password)
			u.set_password(password)
			u.save()
			subject = 'Password Reset'
			from_email= settings.EMAIL_HOST_USER
			to_email = [email]
			message = 'hi, your new password is ' + password
			send_mail(subject, message, from_email, to_email, fail_silently = False )
			return redirect('account:reset_password_confirm')
		else:
			return HttpResponse('Invalid Email Address')
	else:
		form = EmailPasswordReset()
	return render(request, 'account/reset_password.html', {'form':form})

def reset_password_confirm(request):
	return render(request, 'account/reset_password_email2.html', {})
def change_password(request):
	if request.method == 'POST':
		form = ChangePasswordCodeForm(request.POST)
		if form.is_valid():
			# try:
			email = form.cleaned_data.get('user_email')
			detail = ChangePasswordCode.objects.filter(user_email=email)
			if detail.exists():
				# messages.add_message(request, messages.INFO, 'invalid')
				for i in detail:
					i.delete()
				form.save()
				test = ChangePasswordCode.objects.get(user_email=email)
				subject = "Change Password"
				from_email = settings.EMAIL_HOST_USER
				# Now we get the list of emails in a list form.
				to_email = [email]
				#Opening a file in python, with closes the file when its done running
				detail2 = "https://www.atreat4u.com.ng/accounts/"+ str(test.user_id)
				with open(settings.BASE_DIR + "/templates/account/change_password_email.txt") as sign_up_email_txt_file:
					sign_up_message = sign_up_email_txt_file.read()
				message = EmailMultiAlternatives(subject=subject, body=sign_up_message,from_email=from_email, to=to_email )
				html_template = get_template("account/change_password_email.html").render({'detail2':detail2})
				message.attach_alternative(html_template, "text/html")
				message.send()
				return redirect('account:change_password_confirm')
			else:
				form.save()
				test = ChangePasswordCode.objects.get(user_email=email)
				subject = "Change Password"
				from_email = settings.EMAIL_HOST_USER
				# Now we get the list of emails in a list form.
				to_email = [email]
				#Opening a file in python, with closes the file when its done running
				detail2 = "https//www.atreat4u.com.ng/accounts/"+ str(test.user_id)
				with open(settings.BASE_DIR + "/templates/account/change_password_email.txt") as sign_up_email_txt_file:
					sign_up_message = sign_up_email_txt_file.read()
				message = EmailMultiAlternatives(subject=subject, body=sign_up_message,from_email=from_email, to=to_email )
				html_template = get_template("account/change_password_email.html").render({'detail2':detail2})
				message.attach_alternative(html_template, "text/html")
				message.send()
				send_mail(subject=subject,from_email=from_email, recipient_list=to_email, message=sign_up_message, fail_silently=False)
				return redirect('account:change_password_confirm')

		else:
			return HttpResponse('Invalid Email Address')
	else:
		form = ChangePasswordCodeForm()
	return render(request, 'account/change_password.html', {'form':form})


def change_password_confirm(request):
	return render(request, 'account/change_password_confirm.html', {})
def change_password_code(request, pk):
	test = ChangePasswordCode.objects.get(pk=pk)
	detail_email = test.user_email
	u = User.objects.get(email=detail_email)
	if request.method == 'POST':
		form = ChangePasswordForm(request.POST)
		if form.is_valid():
			u = User.objects.get(email=detail_email)
			new_password = form.cleaned_data.get('new_password')
			confirm_new_password = form.cleaned_data.get('confirm_new_password')


			if new_password == confirm_new_password:
				u.set_password(confirm_new_password)
				u.save()
				test.delete()
				return redirect('account:change_password_success')
			else:
				return HttpResponse('your new password should match with the confirm password')


		else:
			return HttpResponse('Invalid Details')
	else:
		form = ChangePasswordForm()
	return render(request, 'account/change_password_code.html', {'test':test, 'form':form, 'u':u})



def change_password_success(request):
	return render(request, 'account/change_password_success.html', {})
=======
	if request.method == 'POST':
		logout(request)
		return redirect('/')
	return render(request, "account/logout.html", {})
# @login_required


# def dashboard(request):
# 	return render(request, 'account/dashboard.html', {'section': 'dashboard'})
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
