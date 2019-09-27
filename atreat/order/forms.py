<<<<<<< HEAD
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ['RecipientName', 'RecipientPhoneNumber', 'TreatOccasion', 'SpecialNote']
=======
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ['RecipientName', 'RecipientPhoneNumber', 'TreatOccasion', 'SpecialNote']
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
