from __future__ import unicode_literals

from django.db import models

# Create your models here.
# class UserManager(models.Manager):

# 	def userCreate(self, name):
# 		user = User.objects.create(name=name)
# 		return user

class User(models.Model):
	name = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	# objects = UserManager()

# class InterestManager(models.Manager):
# 	def interestCreate(self, interest, name):
# 		user_interest = Interest.objects.create(interest=interest, names="name")
# 		user_interest.name.add(user_interest)
# 		return i

class Interest(models.Model):
	interest = models.CharField(max_length=255)
	names = models.ManyToManyField('User')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	# objects = InterestManager()


