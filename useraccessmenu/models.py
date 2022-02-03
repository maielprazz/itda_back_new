from django.db import models
from django.conf import settings
# from authentication.models import User
# Create your models here.

# Master Data Menu
class MainMenu(models.Model):
	TYPES = [('1','Main'),('2','Parent'),('3','Child')]

	code = models.CharField(max_length=7, blank=False, null=False, default="DEF")
	typ = models.CharField(max_length=6, choices = TYPES, default= 'Child')
	parentCode  = models.CharField(max_length=7, blank=True, null=True)
	desc  = models.CharField(max_length=200, blank=True, null=True)
	text  = models.CharField(max_length=12, blank=False, null=False, default = "TextMenu")
	icon  = models.CharField(max_length=40, blank=False, null=False, default="bx bx-data")
	path  = models.CharField(max_length=40, blank=False, null=False, default="/login")
	badge  = models.CharField(max_length=7, blank=True, null=True)
	badgeContent  = models.CharField(max_length=20, blank=True, null=True)
	createdAt = models.DateField(auto_now_add=True)

	class Meta:
		ordering = ('typ','code',)
	def __str__(self):
		return	str(self.typ) + '-' + str(self.text)

# User access Menu 
class UserAccessMenu(models.Model):
	username = models.CharField(max_length=50)
	email = models.EmailField(max_length=50, blank=True, null=True)
	code = models.CharField(max_length=7, blank=True, null=True)
	typ = models.CharField(max_length=6,blank=True, null=True)
	parentCode = models.CharField(max_length=7,blank=True, null=True)
	desc = models.CharField(max_length=200, blank=True, null=True)
	text = models.CharField(max_length=12, blank=True, null=True)
	icon = models.CharField(max_length=40, blank=True, null=True)
	path = models.CharField(max_length=40, blank=True, null=True)
	badge = models.CharField(max_length=7, blank=True, null=True)
	badgeContent = models.CharField(max_length=20,blank=True, null=True)
	access = models.BooleanField(null=False, default=False)
	
	class Meta:
		managed = False
		db_table = 'useraccessmenu_map'
		ordering = ('username', 'code',)

	def __str__(self):
		return	str(self.username) + ' on ' + str(self.code)
