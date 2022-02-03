from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from useraccessmenu.models import MainMenu, UserAccessMenu 
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_save_create_user(sender, instance, created, **kwargs):
  
  menu_set = MainMenu.objects.all()
  username = instance.username
  email = instance.email
  objs = []

  for menu in menu_set.iterator():
    if not UserAccessMenu.objects.filter(username = username).filter(code = menu.code).first():
      if menu.code == "HOM":
        access = True
      else:
        access = False
      objs.append(UserAccessMenu(username= username, email = email, code = menu.code, typ = menu.typ, parentCode = menu.parentCode, desc = menu.desc, text = menu.text, icon = menu.icon, path = menu.path, badge = menu.badge, badgeContent = menu.badgeContent, access = access))

  UserAccessMenu.objects.bulk_create(objs)

@receiver(post_save, sender=MainMenu)
def post_save_create_main_menu(sender, instance, created, **kwargs):
  
  user_set = User.objects.all()
  code = instance.code
  typ = instance.typ
  icon = instance.icon
  parentCode = instance.parentCode
  desc = instance.desc
  text = instance.text
  path = instance.path
  badge = instance.badge
  badgeContent = instance.badgeContent

  objs = []

  for usr in user_set.iterator():
    if not UserAccessMenu.objects.filter(username = usr.username).filter(code = code).first():

      if usr.username == "test" or usr.username == "Ismail.prasetyo":
        access = True
      else:
        access = False
 

      if parentCode and typ == 1:
        parentCode = ''
      objs.append(UserAccessMenu(username= usr.username, email = usr.email, code = code, typ = typ, parentCode = parentCode, desc = desc, text = text, icon = icon, path = path, badge = badge, badgeContent = badgeContent, access = access))

  UserAccessMenu.objects.bulk_create(objs)
