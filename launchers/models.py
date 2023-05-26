from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class LoginHistory(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	ip = models.CharField(max_length=100,blank=True, null=True)
	login_time = models.CharField(max_length=100,blank=True, null=True)
	logout_time = models.CharField(max_length=200,blank=True, null=True)
	created_at = models.DateField(default=timezone.now)
	start_break = models.CharField(max_length=200,blank=True, null=True)
	stop_break = models.CharField(max_length=200,blank=True, null=True)
	def __str__(self):
		return str(self.user)

class break_times(models.Model):
	datetime = models.DateTimeField(default=datetime.now)
	date_today = models.CharField(max_length=100,blank=True, null=True)
	name = models.CharField(max_length=200,blank=True, null=True)
	start_break = models.CharField(max_length=200,blank=True, null=True)
	stop_break = models.CharField(max_length=200,blank=True, null=True)
	def __str__(self):
		return str(self.name)

class User_Profile(models.Model):
	name = models.CharField(max_length=200,blank=True, null=True)
	last_name = models.CharField(max_length=200,blank=True, null=True)
	Email = models.CharField(max_length=200,blank=True, null=True)
	contact_number = models.CharField(max_length=200,blank=True, null=True)
	profile_pic = models.ImageField(upload_to='images/')
	office_email = models.EmailField(max_length=200)
	def __str__(self):
		return str(self.office_email)

class Profile(models.Model):
	inquiry_status  = models.CharField(max_length=200,blank=True, null=True)
	application  = models.CharField(max_length=200,blank=True, null=True)
	visa  = models.CharField(max_length=200,blank=True, null=True)
	userid = models.CharField(max_length=200,primary_key=True)
	advisor = models.CharField(max_length=100,blank=True, null=True)
	reference = models.CharField(max_length=200,blank=True, null=True)
	prefix = models.CharField(max_length=200,blank=True, null=True)
	first_name = models.CharField(max_length=200,blank=True, null=True)
	middle_name = models.CharField(max_length=200,blank=True, null=True)
	last_name = models.CharField(max_length=200,blank=True, null=True)
	dob = models.CharField(max_length=200,blank=True, null=True)
	Email = models.EmailField(max_length=200,blank=True, null=True)
	contact_number = models.CharField(max_length=200,blank=True, null=True)
	Address = models.CharField(max_length=200,blank=True, null=True)
	correspondence_address = models.CharField(max_length=200,blank=True, null=True)
	Nationality = models.CharField(max_length=200,blank=True, null=True)
	Gender = models.CharField(max_length=200,blank=True, null=True)
	Marital_Status = models.CharField(max_length=200,blank=True, null=True)
	Country_Preference_a = models.CharField(max_length=200,blank=True, null=True)
	Country_Preference_b = models.CharField(max_length=200,blank=True, null=True)
	Others_Country = models.CharField(max_length=200,blank=True, null=True)
	intake  = models.CharField(max_length=200,blank=True, null=True)
	month  = models.CharField(max_length=200,blank=True, null=True)
	year  = models.CharField(max_length=200,blank=True, null=True)
	week  = models.CharField(max_length=200,blank=True, null=True)
	datetime = models.DateTimeField(default=datetime.now)
	def __str__(self):
		return str(self.userid)
		
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage(location='/media/')

class Documents(models.Model): 
	userid = models.ForeignKey(Profile, on_delete=models.CASCADE)
	Class_10 = models.FileField(upload_to='media/',blank=True, null=True)
	Class_12 = models.FileField(upload_to='media/',blank=True, null=True)
	Passport_Front = models.FileField(upload_to='media/',blank=True, null=True)
	Visa_Stamp = models.FileField(upload_to='media/',blank=True, null=True)
	Graduation_Marksheet = models.FileField(upload_to='media/',blank=True, null=True)
	Resume = models.FileField(upload_to='media/',blank=True, null=True)
	Others = models.FileField(upload_to='media/',blank=True, null=True)
	def __str__(self):
		return str(self.userid)


class Followup(models.Model): 
	userid = models.ForeignKey(Profile, on_delete=models.CASCADE)
	advisor =  models.CharField(max_length=200,blank=True, null=True)
	next_followup_notification = models.CharField(max_length=200,blank=True, null=True)
	last_follow_up_text =  models.CharField(max_length=10000,blank=True, null=True)
	lastfollowupdate = models.DateTimeField(default=datetime.now)
	def __str__(self):
		return str(self.userid)
	
class FileNote(models.Model): 
	userid = models.ForeignKey(Profile, on_delete=models.CASCADE)
	date = models.DateTimeField(default=datetime.now)
	note = models.CharField(max_length=10000,blank=True, null=True)
	advisor = models.CharField(max_length=200,blank=True, null=True)
	file_note_date = models.CharField(max_length=200,blank=True, null=True)
	add_file_datetime = models.CharField(max_length=200,blank=True, null=True)
	def __str__(self):
		return str(self.userid)

class LeadStage(models.Model): 
	userid = models.ForeignKey(Profile, on_delete=models.CASCADE)
	date = models.DateField()

class idinfo(models.Model):
	userid = models.CharField(max_length=200,blank=True, null=True)
	datetime = models.DateTimeField(default=datetime.now)
	# def __str__(self):
	# 	return self.first_name

class country(models.Model):
	allcountry = models.CharField(max_length=200,blank=True, null=True)
	def __str__(self):
		return self.allcountry
