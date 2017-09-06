from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

status = (
		('Pending','Pending'),
		('Sanctioned','Sanctioned'),
		('Rejected','Rejected')
	)
class UserProfile(models.Model):

	user = models.OneToOneField(User,on_delete=models.CASCADE)
	name = models.CharField(max_length=128)
	designation = models.CharField(max_length=128)
	seqno = models.IntegerField(default=0)
	contact = models.CharField(blank=True,max_length=128)
	def __unicode__(self):
		return self.user.username


class Vehicle(models.Model):

		veh_name = models.CharField(max_length=128)
		capacity = models.CharField(max_length=30)
		image = models.ImageField(upload_to='veh_pics',blank=True)
		def __unicode__(self):
			return self.veh_name


class UserInbox(models.Model):

	
	user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
	veh = models.ForeignKey(Vehicle,null=True)
	app_no = models.CharField(max_length=128)
	app_sub_time = models.DateTimeField(auto_now=False,auto_now_add=True)
	date_of_journey = models.DateField(blank=False)
	from_time = models.TimeField(blank=True)
	to_time = models.TimeField(blank=True)
	purpose = models.CharField(max_length=128)
	source = models.CharField(max_length=128)
	destination = models.CharField(max_length=128,blank=True)
	others = models.CharField(max_length=128)
	status = models.CharField(max_length=30,choices=status,default='Pending')
	
	def __unicode__(self):
		return self.app_no
	

class Slot(models.Model):

	veh = models.ForeignKey(Vehicle,null=True)
	from_t = models.TimeField(blank=True)
	to_t = models.TimeField(blank=True)
			
		
	def __unicode__(self):
		return self.from_t

class FeedBack(models.Model):

	fb_no = models.CharField(max_length=128)
	user = models.ForeignKey(UserProfile,null=True)
	Suggestions = models.CharField(max_length=128)
	Remarks = models.CharField(max_length=128)
	status = models.IntegerField(default=0)
	fb_sub_time = models.DateTimeField(auto_now=False,auto_now_add=True)
	

	def __unicode__(self):
		return self.fb_no

class FeedbackReply(models.Model):

	feedback = models.ForeignKey(FeedBack,null=True)
	reply = models.CharField(max_length=128)
	reply_sub_time = models.DateTimeField(auto_now=False,auto_now_add=True)

	def __unicode__(self):
		return self.reply