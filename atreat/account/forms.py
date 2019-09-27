from django.contrib.auth.models import User
from django import forms
<<<<<<< HEAD
from .models import PasswordResetEmail, ChangePassword, ChangePasswordCode, CreateProfie
from django.contrib.auth import authenticate



class CreateProfieForm1(forms.ModelForm):
    class Meta:
        model = CreateProfie
        fields = ['first_name', 'last_name', 'phone']

class RegisterForm(forms.Form):
    username = forms.CharField()

    # image = forms.FileField()
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Enter First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Enter Last Name'}))
    phone_number = forms.IntegerField()
    email    = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
=======




	
class RegisterForm(forms.Form):
    username = forms.CharField()
    email    = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
    def clea_pass(self):
    	cd = self.cleaned_data
    	if cd['password'] != cd['password2']:
    		raise forms.ValidationError('Passwords don\'t match.')
    	return cd['password']


    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email
class LoginForm(forms.Form):
<<<<<<< HEAD
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder':'Enter Password'}))
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password :
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Invalid Log in details. Try Again....")
            if not user.is_active:
                raise forms.ValidationError("This User is no longer active.")
            return super(LoginForm, self).clean(*args, **kwargs)

    # username = forms.CharField(label='Email')
    # password = forms.CharField(widget=forms.PasswordInput)



class EmailPasswordReset(forms.ModelForm):
    class Meta:
        model = PasswordResetEmail
        fields = ['email']
        widgets = {
            'email':forms.EmailInput(),
        }


class ChangePasswordCodeForm(forms.ModelForm):
    class Meta:
        model = ChangePasswordCode
        fields = ['user_email']
        widgets = {
                    'user_email': forms.EmailInput(),
        }

class ChangePasswordForm(forms.ModelForm):
    class Meta:
        model = ChangePassword
        fields = ['new_password', 'confirm_new_password']
        widgets = {
                    'new_password':forms.PasswordInput(),
                    'confirm_new_password':forms.PasswordInput(),
        }
=======
    # username = forms.CharField()
    username = forms.CharField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c

