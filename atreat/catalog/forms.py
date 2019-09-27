from django import forms
from .models import Meal, Cbid, MusicBid, BusinessBid, TvhostBid

class MealForm(forms.ModelForm):
	class Meta:
		model = Meal
<<<<<<< HEAD
		fields = ['restaurant', 'location', 'Menu', 'Brand', 'Size', 'Amount' ]
=======
		fields = ['restaurant', 'real_restaurant', 'location', 'Menu', 'Brand', 'Size', 'Amount' ]
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
class CbidForm(forms.ModelForm):
	class Meta:
		model = Cbid
		fields = ['amount', 'celeb', 'user']
		widgets = {'celeb':forms.HiddenInput(), 'user':forms.HiddenInput()}
class MusicBidForm(forms.ModelForm):
	class Meta:
		model = MusicBid
		fields = ['amount', 'celeb', 'user']
		widgets = {'celeb':forms.HiddenInput(), 'user':forms.HiddenInput()}
class BusinessBidForm(forms.ModelForm):
	class Meta:
		model = BusinessBid
		fields = ['amount', 'celeb', 'user']
		widgets = {'celeb':forms.HiddenInput(), 'user':forms.HiddenInput()}
class TvhostBidForm(forms.ModelForm):
	class Meta:
		model = TvhostBid
		fields = ['amount', 'celeb', 'user']
		widgets = {'celeb':forms.HiddenInput(), 'user':forms.HiddenInput()}

<<<<<<< HEAD



=======
		


	
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
