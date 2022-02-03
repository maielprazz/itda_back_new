from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.db.models.deletion import CASCADE
from helpers.models import TrackingModel
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from useraccessmenu.models import UserAccessMenu

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, UserManager
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse

class ItdaUserManager(UserManager):
	def _create_user(self, username, email, password, **extra_fields):

			if not username:
					raise ValueError('The given username must be set')
			if not email:
					raise ValueError('The given email must be set')		
			email = self.normalize_email(email)
			username = self.model.normalize_username(username)
			user = self.model(username=username, email=email, **extra_fields)
			user.password = make_password(password)
			user.save(using=self._db)
			return user

	def create_user(self, username, email=None, password=None, **extra_fields):
			extra_fields.setdefault('is_staff', False)
			extra_fields.setdefault('is_superuser', False)
			return self._create_user(username, email, password, **extra_fields)

	def create_superuser(self, username, email=None, password=None, **extra_fields):
			extra_fields.setdefault('is_staff', True)
			extra_fields.setdefault('is_superuser', True)

			if extra_fields.get('is_staff') is not True:
					raise ValueError('Superuser must have is_staff=True.')
			if extra_fields.get('is_superuser') is not True:
					raise ValueError('Superuser must have is_superuser=True.')

			return self._create_user(username, email, password, **extra_fields)	


class User(AbstractBaseUser, PermissionsMixin, TrackingModel):
	username_validator = UnicodeUsernameValidator()

	username = models.CharField(
			_('username'),
			max_length=150,
			unique=True,
			help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
			validators=[username_validator],
			error_messages={
					'unique': _("A user with that username already exists."),
			},
	)
	first_name = models.CharField(_('first name'), max_length=150, blank=True)
	last_name = models.CharField(_('last name'), max_length=150, blank=True)
	display_name = models.CharField(_('display name'), max_length=200, blank=True)
	email = models.EmailField(_('email address'), blank=True)
	employeeID=models.CharField(max_length=20, null=True,blank=True)
	is_staff = models.BooleanField(
			_('staff status'),
			default=False,
			help_text=_('Designates whether the user can log into this admin site.'),
	)
	is_active = models.BooleanField(
			_('active'),
			default=True,
			help_text=_(
					'Designates whether this user should be treated as active. '
					'Unselect this instead of deleting accounts.'
			),
	)
	is_verified = models.BooleanField(
			_('user_verified'),
			default=True,
			help_text=_(
					'Designates whether this user should be treated as verified. '
					'Unselect this instead of deleting accounts.'
			),
	)
	date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

	objects = ItdaUserManager()

	EMAIL_FIELD = 'email'
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']
	
	# @property
	# def tokens(self):
	# 	token = RefreshToken.for_user(self)
	# 	# token = ItdaTokenObtainPairSerializer.for_user(self)
	# 	return {
	# 		"refresh": str(token),
	# 		"access": str(token.access_token)
	# 	}

	@property
	def get_drawer(self):
		drwmenu = []
		menus = UserAccessMenu.objects.filter(username = self.username).filter(typ = 1).filter(access__gt=0)
		for menu in menus.iterator():
			menuobj = {}
			menuobj.update({"id":menu.id})
			menuobj.update({"text":menu.text})
			menuobj.update({"icon":menu.icon})
			menuobj.update({"badge":menu.badge})
			
			submenus = UserAccessMenu.objects.filter(username = self.username).filter(access__gt=0).filter(typ = 3).filter(parentCode = menu.code)
			drwsubmenu = []
			for submenu in submenus.iterator():
				submenuobj = {}
				submenuobj.update({"id": submenu.id}) 
				submenuobj.update({"text": submenu.text}) 
				submenuobj.update({"icon": submenu.icon}) 
				submenuobj.update({"path": submenu.path}) 
				submenuobj.update({"badge": submenu.badge}) 
				submenuobj.update({"badgeContent": submenu.badgeContent}) 
				drwsubmenu.append(submenuobj)
			
			menuobj.update({"submenu": drwsubmenu}) 
			drwmenu.append(menuobj)

		# return {'drwmenu': drwmenu}
		return drwmenu
	@property
	def get_accesscode(self):
			menuset = UserAccessMenu.objects.filter(email = self.email)
			accesscode = ''
			for menu in menuset.iterator():
				accesscode = accesscode + '_' + str(menu.code)
			return str(accesscode)

	def __str__(self):
		return self.username	



