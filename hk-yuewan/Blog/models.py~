from django.db import models
class Msg(models.Model):
	ip = models.GenericIPAddressField()
	title = models.CharField(max_length=50)
	content = models.CharField(max_length=9999)
	date = models.DateTimeField(auto_now_add=True)
	author = models.CharField(max_length=20)
	StartTime = models.DateTimeField()
	EndTime = models.DateTimeField()
	people = models.IntegerField(default=0)
	peoplelist = models.CharField(max_length=999,default='PeopleList:')
	def __unicode__(self):
		return self.title
	class Meta:
		ordering = ['-date']
