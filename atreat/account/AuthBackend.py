<<<<<<< HEAD
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class EmailAuthBackend(object):

	def authenticate(self, request, username=None, password=None):
		try:
			user = User.objects.get(email=username)
			if user.check_password(password):
				return user
			else:
				return None
		except User.DoesNotExist:
			raise ValidationError('invalid credentials')
	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None


=======
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class EmailAuthBackend(object):

	def authenticate(self, request, username=None, password=None):
		try:
			user = User.objects.get(email=username)
			if user.check_password(password):
				return user
			else:
				return None
		except User.DoesNotExist:
			raise ValidationError('invalid credentials')
	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None


>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
