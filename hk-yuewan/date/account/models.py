from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
class Profile(models.Model):
	user = models.ForeignKey(User , unique = True)
	realname = models.CharField(max_length = 10)
	signature = models.CharField(max_length = 200)
	mobile = models.CharField(max_length = 11)
	sex = models.CharField(max_length = 5)

	def __unicode__(self):
		return self.user.username

	class Meta:
		db_table = 'account_profile'