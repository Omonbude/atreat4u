<<<<<<< HEAD
from django import forms
from .models import CelebrityBid, RebidCeleb, MealQuantity, CinemaQuantity

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
	quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
	update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class CelebBid(forms.ModelForm):
	class Meta:
		model = CelebrityBid
		fields = ['amount']
class CelebRebid(forms.ModelForm):
	class Meta:
		model = RebidCeleb
		fields = ['amount']
class MealQuantityForm(forms.ModelForm):
	class Meta:
		model = MealQuantity
		fields = ['quantity']
class CinemaQuantityForm(forms.ModelForm):
	class Meta:
		model = CinemaQuantity
=======
from django import forms
from .models import CelebrityBid, RebidCeleb, MealQuantity, CinemaQuantity

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
	quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
	update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class CelebBid(forms.ModelForm):
	class Meta:
		model = CelebrityBid
		fields = ['amount']
class CelebRebid(forms.ModelForm):
	class Meta:
		model = RebidCeleb
		fields = ['amount']
class MealQuantityForm(forms.ModelForm):
	class Meta:
		model = MealQuantity
		fields = ['quantity']
class CinemaQuantityForm(forms.ModelForm):
	class Meta:
		model = CinemaQuantity
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
		fields = ['quantity']