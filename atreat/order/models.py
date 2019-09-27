<<<<<<< HEAD
from django.db import models

class Order(models.Model):
	RecipientName = models.CharField(max_length=50)
	RecipientPhoneNumber = models.CharField(max_length=50)
	TreatOccasion = models.CharField(max_length=50, help_text = 'e.g birthday, marriage, matric etc..')
	SpecialNote = models.TextField(max_length=30, help_text='not more than 30 words')
	user = models.CharField(max_length=50)

	def __str__(self):
		return self.RecipientName

=======
from django.db import models

class Order(models.Model):
	RecipientName = models.CharField(max_length=50)
	RecipientPhoneNumber = models.CharField(max_length=50)
	TreatOccasion = models.CharField(max_length=50, help_text = 'e.g birthday, marriage, matric etc..')
	SpecialNote = models.TextField(max_length=30, help_text='not more than 30 words')
	user = models.CharField(max_length=50)

	def __str__(self):
		return self.RecipientName

>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
