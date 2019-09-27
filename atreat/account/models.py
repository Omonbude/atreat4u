from django.db import models
<<<<<<< HEAD
import uuid
class PasswordResetEmail(models.Model):
	email = models.EmailField()
class ChangePasswordCode(models.Model):
	user_email = models.EmailField(max_length=50)
	user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
class ChangePassword(models.Model):
	new_password = models.CharField(max_length=50, blank = False, null = False)
	confirm_new_password = models.CharField(max_length=50, blank = False, null = False)
class CreateProfie(models.Model):
	user = models.CharField(max_length=50, unique=True)
	email = models.EmailField()
	image = models.FileField()
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	phone = models.CharField(max_length=20)
	def __str__(self):
		return self.first_name + ' ' + self.last_name
=======

# Create your models here.
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
