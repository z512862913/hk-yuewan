from django.db import models
from django.contrib.auth.models import AbstractUser, User

class Account(AbstractUser):
	realname = models.CharField(max_length = 10)
	signature = models.CharField(max_length = 200)
	mobile = models.CharField(max_length = 11)
	sex = models.CharField(max_length = 5)

	def __unicode__(self):
		return self.user.username