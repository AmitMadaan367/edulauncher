from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import time
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from django.shortcuts import redirect
from datetime import date
import socket
from .models import *
from datetime import timedelta
from django.db.models.functions import TruncDay
from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.views import APIView
from rest_framework.response import Response
from bs4 import BeautifulSoup
from django.core.mail import send_mail
from django.conf import settings
import pandas as pd 
import os, tempfile, zipfile
from wsgiref.util import FileWrapper
from io import StringIO
import csv  




@login_required
def csv_download_Leads(request):
	User_id = []
	user_na = []
	mobiles = []
	us_status = []
	emailsss = []
	date_feed = []
	time_feed = []
	all_userss = Profile.objects.all().order_by('datetime').reverse()
	for cs in all_userss:
		if cs.inquiry_status == 'Lead':
			if cs.first_name and cs.last_name:
				nam = cs.first_name + ' ' + cs.last_name
				user_na.append(nam)
			else:
				if cs.last_name == None or cs.last_name == '':
					user_na.append(cs.first_name)
			User_id.append(cs.userid)
			if cs.application == 'submitted' or cs.application == 'submitted ':
				us_status.append('Application '+cs.application)
			elif cs.application == 'apply ' or cs.application == 'apply':
				us_status.append('Offer '+cs.application)
			elif cs.application == 'progress ' or cs.application == 'progress':
				us_status.append('Application in '+cs.application)
			elif cs.application == 'declined ' or cs.application == 'declined':
				us_status.append('Offer '+cs.application)
			elif cs.application == '' or cs.application == None:
				us_status.append(None)

				
			mobiles.append(cs.contact_number)
			if cs.Email == None or cs.Email == '':
				emailsss.append(None)
			else:
				emailsss.append(cs.Email)
			
			try:
			# print(str(cs.datetime).split(" ")[0].split('-'))
				day = str(cs.datetime).split(" ")[0].split('-')[2]
				months = str(cs.datetime).split(" ")[0].split('-')[1]
				year = str(cs.datetime).split(" ")[0].split('-')[0]
				print(day+'-'+months+'-'+year)
				dates = day+'-'+months+'-'+year
				date_feed.append(dates)
				time_feed.append(str(cs.datetime).split(" ")[1].split('.')[0])
				print(time_feed)
			except:
				day = str(cs.datetime).split(" ")[0].split('-')[2]
				months = str(cs.datetime).split(" ")[0].split('-')[1]
				year = str(cs.datetime).split(" ")[0].split('-')[0]
				print(day+'-'+months+'-'+year)
				dates = day+'-'+months+'-'+year
				date_feed.append(dates)
				time_feed.append(str(cs.datetime).split(" ")[1].split('.')[0])
				print(time_feed)
				pass
	print(len(User_id),len(time_feed),len(date_feed),len(user_na),len(mobiles),len(emailsss),len(us_status))
	df=pd.DataFrame({'User Id':User_id,'Username':user_na,'Phone Number':mobiles,'Email':emailsss,'Status':us_status,'Date':date_feed,'Time':time_feed})
	df.to_csv('Leads.csv',index=True)
	filename     = "Leads.csv" # Select your file here.
	wrapper      = FileWrapper(open(filename))
	response = HttpResponse(content_type='csv')
	filename = "Leads.csv".format("data")
	fp = StringIO()
	response = HttpResponse(content_type='csv')
	response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
	writer =df.to_csv(response)

	return response

@login_required
def csv_download_inq(request):
	User_id = []
	user_na = []
	mobiles = []
	us_status = []
	emailsss = []
	date_feed = []
	time_feed = []
	all_userss = Profile.objects.all().order_by('datetime').reverse()
	for cs in all_userss:
		if cs.inquiry_status == 'Hot' or cs.inquiry_status == 'Cold' or cs.inquiry_status == 'Warm' or cs.inquiry_status == ' ' or cs.inquiry_status == None or cs.inquiry_status == '':
			if cs.first_name and cs.last_name:
				nam = cs.first_name + ' ' + cs.last_name
				user_na.append(nam)
			else:
				if cs.last_name == None or cs.last_name == '':
					user_na.append(cs.first_name)
					print(cs.first_name)
			User_id.append(cs.userid)
			us_status.append(cs.inquiry_status)
			mobiles.append(cs.contact_number)
			if cs.Email == None or cs.Email == '':
				emailsss.append(None)
			else:
				emailsss.append(cs.Email)
			print(cs.first_name)
			try:
			# print(str(cs.datetime).split(" ")[0].split('-'))
				day = str(cs.datetime).split(" ")[0].split('-')[2]
				months = str(cs.datetime).split(" ")[0].split('-')[1]
				year = str(cs.datetime).split(" ")[0].split('-')[0]
				print(day+'-'+months+'-'+year)
				dates = day+'-'+months+'-'+year
				date_feed.append(dates)
				time_feed.append(str(cs.datetime).split(" ")[1].split('.')[0])
				print(time_feed)
			except:
				day = str(cs.datetime).split(" ")[0].split('-')[2]
				months = str(cs.datetime).split(" ")[0].split('-')[1]
				year = str(cs.datetime).split(" ")[0].split('-')[0]
				print(day+'-'+months+'-'+year)
				dates = day+'-'+months+'-'+year
				date_feed.append(dates)
				time_feed.append(str(cs.datetime).split(" ")[1].split('.')[0])
				print(time_feed)
				pass

	df=pd.DataFrame({'User Id':User_id,'Username':user_na,'Phone Number':mobiles,'Email':emailsss,'Status':us_status,'Date':date_feed,'Time':time_feed})
	df.to_csv('Inquiry.csv',index=True)
	filename     = "Inquiry.csv" # Select your file here.
	wrapper      = FileWrapper(open(filename))
	response = HttpResponse(content_type='csv')
	filename = "Inquiry.csv".format("data")
	fp = StringIO()
	response = HttpResponse(content_type='csv')
	response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
	writer =df.to_csv(response)

	return response




@login_required
def change_statusss(request):
	chnage = request.POST.get('status')
	print('chnage',chnage.split('EDUAL'))
	ids = 'EDUAL'+chnage.split('EDUAL')[1]
	idsd = chnage.split('EDUAL')[0]
	print(idsd)
	obj_status = Profile.objects.get(userid=ids)
	obj_status.visa = idsd
	obj_status.save()
	return HttpResponseRedirect('/apply/')
@login_required
def applyed(request):
	users = Profile.objects.all().order_by('datetime').reverse()
	show_user = []
	for user_info in users:
		show_user.append(user_info.first_name)
	from datetime import date
	today = date.today()
	update_obj = FileNote.objects.filter(file_note_date=today)
	lenth = []
	ids_user = []
	today_follow = []
	username_s = []
	bday = Profile.objects.all()
	ss = str(today)
	for brith in bday:
		try:
			if brith.dob[5:] == ss[5:]:
				if brith.last_name == None or brith.last_name == '':
					print(brith.first_name)
					username_ids = brith.first_name
					ids_user.append(username_ids)
				else:
					lenth.append(brith.dob)
					username_id = str(brith.first_name)+' '+str(brith.last_name)
					ids_user.append(username_id)
					username_s.append('Birthday')
		except:
			pass
	for data in update_obj:
		lenth.append(data.file_note_date)
		ids_user.append(data.userid)
		nameusera = Profile.objects.get(userid=data.userid)
		username_ids = nameusera.last_name
		if username_ids == None:
			username_ids = nameusera.first_name
			username_s.append(username_ids)
		else:
			username_id = str(nameusera.first_name)+' '+str(nameusera.last_name)
			username_s.append(username_id)
		today_follow.append(data.file_note_date)
	if len(lenth) == 0:
		notify = 0
	else:
		notify = len(lenth)
	loginuser = User.objects.get(username=request.user.username)
	ss = str(loginuser)
	split = ss.split('@' '')[0]
	try:
		img = User_Profile.objects.get(office_email=ss)
		if img.profile_pic == '':
			img = 'h' 
			imagedummy = 'h'
		else:
			img = User_Profile.objects.all().filter(office_email=ss)
			img = img
			imagedummy = 'h'
	except:
		img = User_Profile.objects.all().filter(office_email=ss)
		ss = len(img)
		if len(img) == 0:
			img = 'h'
			imagedummy = 'h'
	all_datils = zip(ids_user,username_s)

	loginuser = User.objects.get(username=request.user.username)
	chahat = str(loginuser)
	user = Profile.objects.all()
	user = reversed(user)
	user_ids = []
	fullname = []
	allid =[]
	# users = Followup.objects.all()
	idsnew=[]
	datenew=[]
	references = []
	user_ids_login = []
	Emailsa = []
	contact_numbers = []
	firstnames = []
	status_s = []
	all_user_s = []
	for detail in user:
		qs = detail.inquiry_status
		if qs == 'Offer accepted':
			all_user = Profile.objects.get(userid=detail.userid)
			print(all_user)
			all_user_s.append(all_user)
			ids = detail.userid
			allid.append(ids)
			datetime = detail.datetime
			date = datetime.strftime("%Y-%m-%d %H:%M")
			idsnew.append(ids)
			datenew.append(date)
			references.append(detail.reference)
			ddddd = detail.advisor
			try:
				user_admin = ddddd.split('@' '')[0]
			except:
				user_admin = detail.advisor
			user_ids_login.append(user_admin)
			first_ = detail.first_name
			last_ = detail.last_name
			if last_ ==  None:
				name = first_
			else:
				name = str(first_)+' '+str(last_)
			Emails = detail.Email
			contact_number = detail.contact_number
			fullname.append(name)
			Emailsa.append(Emails)
			contact_numbers.append(contact_number)
			status_s.append(detail.inquiry_status)
			firstnames.append(first_)
			
	lens1=len(user_ids)
	lens2=len(fullname)
	maxx=max([lens1,lens2])
	for i in range(1, maxx+1):
		if len(user_ids) <i:
			user_ids.append("")
		if len(fullname) <i:
			fullname.append("")
	Offices = 'Office'
	Facebooks = 'Facebook'
	loginusers = str(loginuser)
	userss = loginusers.split('@' '')[0]
	alldetail = zip(idsnew,datenew,references,user_ids_login,fullname,Emailsa,contact_numbers,status_s)
	warm = 'Warm'
	# page = request.GET.get('page', 1)
	# paginator = Paginator(all_user_s, 30)
	# try:
	# 	users = paginator.page(page)
	# except PageNotAnInteger:
	# 	users = paginator.page(1)
	# except EmptyPage:
	# 	users = paginator.page(paginator.num_pages)

	

	if 'chahat@edulaunchers.com' in chahat:
		return render(request, 'apply1.html',{'warsm':warm,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'alldetails':alldetail,'user_ids':allid,'loginuser':loginusers,'Offices':Offices,'Facebooks':Facebooks,'firstnames':firstnames,'image':imagedummy,'show_user':show_user,'users':users})
	else:
		return render(request, 'apply.html',{'hotel_images' : img,'notify':notify,'all_datils':all_datils,'alldetails':alldetail,'user_ids':allid,'loginuser':loginusers,'Offices':Offices,'Facebooks':Facebooks,'firstnames':firstnames,'image':imagedummy,'show_user':show_user,'users':users})





def setpassword(request):
	chnage = request.GET.get('email')
	if request.method == 'POST':
		new = request.POST['js']
		olds = request.POST['aak']
		print(new,olds)
		if new == olds:
			print(new,olds)
			u = User.objects.get(username__exact=chnage)
			print(u)
			u.set_password(new)
			u.save()
			return HttpResponseRedirect('/')
	return render(request, 'reset.html')	

def forgotpassword(request):
	if request.method == 'POST':
		email = request.POST['emails']
		print(email)
		subject = 'Password Change Request'
		message = f"Please clieck on the link and change the password. https://edulauncher.herokuapp.com/setpassword/?email="+(email)
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [email, ]
		send_mail( subject, message, email_from, recipient_list )
		sh = 'Please check your email and change the password'
		if email != '':
			return render(request, 'forgot.html',{'sh':sh})
	
	return render(request, 'forgot.html')


@login_required
def change_status(request):
	chnage = request.GET.get('status')
	print('chnage',chnage)
	inq = chnage.split(' ' '')[0]
	ids = chnage.split(' ' '')[1]
	obj_status = Profile.objects.get(userid=ids)
	obj_status.inquiry_status = inq
	obj_status.save()
	return HttpResponseRedirect('/enquiry/')


@login_required
def change_statuss(request):
	chnage = request.POST.get('status')
	st = chnage.split('EDUAL')[0]
	if request.method == 'POST':
		try:
			respostaum = request.POST['showhideinput']
			print("dffsd")
			if respostaum != '':
				ids = 'EDUAL'+chnage.split('EDUAL')[1]
				obj_stat = Profile.objects.get(userid=ids)
				cah = 'Offer accepted'
				offer = 'Offer accepted '+respostaum
				print("offer",offer)
				obj_stat.inquiry_status = cah
				obj_stat.application = offer 
				obj_stat.save()
				return HttpResponseRedirect('/user/')
			else:
				print("elseeeeeee")
				ids = 'EDUAL'+chnage.split('EDUAL')[1]
				st = chnage.split('EDUAL')[0]
				obj_statuss = Profile.objects.get(userid=ids)
				obj_statuss.application = st
				obj_statuss.save()
				return HttpResponseRedirect('/user/')
		except:
			print("except")
			ids = 'EDUAL'+chnage.split('EDUAL')[1]
			st = chnage.split('EDUAL')[0]
			print(chnage.split('EDUAL'))
			if st == 'Hot ' or st == 'Hot':
				print('st == ',st)
				obj_statuss = Profile.objects.get(userid=ids)
				obj_statuss.inquiry_status = st
				obj_statuss.save()
			else:
				print(st)
				obj_statuss = Profile.objects.get(userid=ids)
				obj_statuss.application = st
				obj_statuss.save()
			return HttpResponseRedirect('/user/')
	
	return HttpResponseRedirect('/user/')

@login_required
def enquiry(request):
	all_user = Profile.objects.all().order_by('datetime').reverse()
	show_user = []
	
	for user_info in all_user:
		show_user.append(user_info.first_name)
	from datetime import date
	today = date.today()
	update_obj = FileNote.objects.filter(file_note_date=today)
	lenth = []
	ids_user = []
	today_follow = []
	username_s = []
	bday = Profile.objects.all()
	ss = str(today)
	for brith in bday:
		try:
			if brith.dob[5:] == ss[5:]:
				if brith.last_name == None or brith.last_name == '':
					print(brith.first_name)
					username_ids = brith.first_name
					ids_user.append(username_ids)
				else:
					lenth.append(brith.dob)
					username_id = str(brith.first_name)+' '+str(brith.last_name)
					ids_user.append(username_id)
					username_s.append('Birthday')
		except:
			pass
	for data in update_obj:
		lenth.append(data.file_note_date)
		ids_user.append(data.userid)
		nameusera = Profile.objects.get(userid=data.userid)
		username_ids = nameusera.last_name
		if username_ids == None:
			username_ids = nameusera.first_name
			username_s.append(username_ids)
		else:
			username_id = str(nameusera.first_name)+' '+str(nameusera.last_name)
			username_s.append(username_id)
		today_follow.append(data.file_note_date)
	if len(lenth) == 0:
		notify = 0
	else:
		notify = len(lenth)
	loginuser = User.objects.get(username=request.user.username)
	ss = str(loginuser)
	split = ss.split('@' '')[0]
	try:
		img = User_Profile.objects.get(office_email=ss)
		if img.profile_pic == '':
			img = 'h' 
			imagedummy = 'h'
		else:
			img = User_Profile.objects.all().filter(office_email=ss)
			img = img
			imagedummy = 'h'
	except:
		img = User_Profile.objects.all().filter(office_email=ss)
		ss = len(img)
		if len(img) == 0:
			img = 'h'
			imagedummy = 'h'
	all_datils = zip(ids_user,username_s)

	loginuser = User.objects.get(username=request.user.username)
	chahat = str(loginuser)
	user = Profile.objects.all().order_by('datetime').reverse()
	user_ids = []
	fullname = []
	allid =[]
	# users = Followup.objects.all()
	idsnew=[]
	datenew=[]
	references = []
	user_ids_login = []
	Emailsa = []
	contact_numbers = []
	firstnames = []
	status_s = []
	all_usersss = []
	for detail in user:
		qs = detail.inquiry_status
		if qs == 'Lead' or qs == 'Offer accepted':
			pass
		else:
			all_user = Profile.objects.get(userid=detail.userid)
			print(all_user)
			all_usersss.append(all_user)
			ids = detail.userid
			allid.append(ids)
			datetime = detail.datetime
			date = datetime.strftime("%Y-%m-%d %H:%M")
			idsnew.append(ids)
			datenew.append(date)
			references.append(detail.reference)
			ddddd = detail.advisor
			try:
				user_admin = ddddd.split('@' '')[0]
			except:
				user_admin = detail.advisor
			user_ids_login.append(user_admin)
			first_ = detail.first_name
			last_ = detail.last_name
			if last_ ==  None:
				name = first_
			else:
				name = str(first_)+' '+str(last_)
			Emails = detail.Email
			contact_number = detail.contact_number
			fullname.append(name)
			Emailsa.append(Emails)
			contact_numbers.append(contact_number)
			status_s.append(detail.inquiry_status)
			firstnames.append(first_)
	lens1=len(user_ids)
	lens2=len(fullname)
	maxx=max([lens1,lens2])
	for i in range(1, maxx+1):
		if len(user_ids) <i:
			user_ids.append("")
		if len(fullname) <i:
			fullname.append("")
	Offices = 'Office'
	Facebooks = 'Facebook'
	loginusers = str(loginuser)
	userss = loginusers.split('@' '')[0]
	alldetail = zip(idsnew,datenew,references,user_ids_login,fullname,Emailsa,contact_numbers,status_s)
	warm = 'Warm'
	page = request.GET.get('page', 1)
	paginator = Paginator(all_usersss, 20)

	try:
		users = paginator.page(page)
	except PageNotAnInteger:
		users = paginator.page(1)
		print(users)
	except EmptyPage:
		users = paginator.page(paginator.num_pages)

	if 'chahat@edulaunchers.com' in chahat:
		return render(request, 'inquiry1.html',{'warsm':warm,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'alldetails':alldetail,'user_ids':allid,'loginuser':loginusers,'Offices':Offices,'Facebooks':Facebooks,'firstnames':firstnames,'image':imagedummy,'show_user':show_user,'users':users})
	else:
		return render(request, 'inquiry.html',{'hotel_images' : img,'notify':notify,'all_datils':all_datils,'alldetails':alldetail,'user_ids':allid,'loginuser':loginusers,'Offices':Offices,'Facebooks':Facebooks,'firstnames':firstnames,'image':imagedummy,'show_user':show_user,'users':users})



def registers(request):
	if request.method == 'POST':
		try:
			pic = request.FILES['myfile']
		except:
			pic = None
		username = request.POST['js']
		password = request.POST['password']
		fname = request.POST['fname']
		lname = request.POST['lname']
		jname = request.POST['zname']
		try:
			user = User.objects.create_user(username=username, password=password)
			user.save()
			p = User_Profile(office_email=username,name=fname,last_name=lname,Email=username,contact_number=jname,profile_pic=pic)
			p.save()
			return HttpResponseRedirect('/')
		except:
			al = 'This user already exists'
			return render(request,'signup.html',{'al':al})
	return render(request,'signup.html')
@login_required
def follow(request):
	today = date.today()
	match = str(today)
	update_obj = FileNote.objects.filter(file_note_date=today)
	lenth = []
	ids_user = []
	today_follow = []
	username_s = []
	follow_id = []
	follow_name = []
	follow_lastname = []
	follow_ids = []
	advisorss = []
	notes = []
	file_note_dates = []
	bday = Profile.objects.all()
	ss = str(today)
	for brith in bday:
		try:
			if brith.dob[5:] == ss[5:]:
				if brith.last_name == None or brith.last_name == '':
					print(brith.first_name)
					lenth.append(brith.dob)
					username_ids = brith.first_name
					ids_user.append(username_ids)
					username_s.append('Birthday')
				else:
					lenth.append(brith.dob)
					username_id = str(brith.first_name)+' '+str(brith.last_name)
					ids_user.append(username_id)
					username_s.append('Birthday')
		except:
			pass

	for data in update_obj:
		lenth.append(data.file_note_date)
		ids_user.append(data.userid)
		nameusera = Profile.objects.get(userid=data.userid)
		username_ids = nameusera.last_name
		if username_ids == None:
			username_ids = nameusera.first_name
			username_s.append(username_ids)
		else:
			username_id = str(nameusera.first_name)+' '+str(nameusera.last_name)
			username_s.append(username_id)
		username_id1 = nameusera.userid
		follow_id.append(username_id1)
		follow_ids.append(username_id1)
		username_id2 = nameusera.first_name
		follow_name.append(username_id2)
		username_id3 = nameusera.last_name
		if username_id3 == None:
			follow_lastname.append('')
		else:
			follow_lastname.append(username_id3)
		advisors = data.advisor
		advisorss.append(advisors)
		note = data.note
		notes.append(note)
		file_note_dates.append(data.file_note_date)
		today_follow.append(data.file_note_date)
	if len(lenth) == 0:
		notify = 0
	else:
		notify = len(lenth)
	if len(follow_name) == 0 and len(follow_id) == 0 and len(follow_lastname) == 0 :
		no = 'No Follow Up Today'
	else:
		no = ''
	show_follow = zip(follow_id,follow_name,follow_lastname,notes,advisorss,file_note_dates)
	loginuser = User.objects.get(username=request.user.username)
	ss = str(loginuser)
	split = ss.split('@' '')[0]
	try:
		img = User_Profile.objects.get(office_email=ss)
		if img.profile_pic == '':
			img = 'h' 
			imagedummy = 'h'
		else:
			print("---")
			img = User_Profile.objects.all().filter(office_email=ss)
			img = img
			imagedummy = 'h'
	except:
		img = User_Profile.objects.all().filter(office_email=ss)
		ss = len(img)
		if len(img) == 0:
			img = 'h'
			imagedummy = 'h'
	chahat = str(loginuser)
	all_datils = zip(ids_user,username_s)
	serchuser = Profile.objects.all()
	show_users_all = []
	for users in serchuser:
		show_users_all.append(users.first_name)
	if 'chahat@edulaunchers.com' in chahat:
		return render(request,'follows1.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'image':imagedummy,'show_users':show_users_all,'show_follow':show_follow,'follow_ids':follow_ids,'no':no})
	else:
		return render(request,'follo.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'image':imagedummy,'show_users':show_users_all,'show_follow':show_follow,'follow_ids':follow_ids,'no':no})		
@login_required
def changepassword(request):
	today = date.today()
	match = str(today)
	update_obj = FileNote.objects.filter(file_note_date=today)
	lenth = []
	ids_user = []
	today_follow = []
	username_s = []
	bday = Profile.objects.all()
	ss = str(today)
	for brith in bday:
		try:
			if brith.dob[5:] == ss[5:]:
				if brith.last_name == None or brith.last_name == '':
					print(brith.first_name)
					lenth.append(brith.dob)
					username_ids = brith.first_name
					ids_user.append(username_ids)
					username_s.append('Birthday')
				else:
					lenth.append(brith.dob)
					username_id = str(brith.first_name)+' '+str(brith.last_name)
					ids_user.append(username_id)
					username_s.append('Birthday')
		except:
			pass
	for data in update_obj:
		lenth.append(data.file_note_date)
		ids_user.append(data.userid)
		nameusera = Profile.objects.get(userid=data.userid)
		username_ids = nameusera.last_name
		if username_ids == None:
			username_ids = nameusera.first_name
			username_s.append(username_ids)
		else:
			username_id = str(nameusera.first_name)+' '+str(nameusera.last_name)
			username_s.append(username_id)
		today_follow.append(data.file_note_date)
	if len(lenth) == 0:
		notify = 0
	else:
		notify = len(lenth)
	loginuser = User.objects.get(username=request.user.username)
	print("loginuser",loginuser)
	print("notify:",notify)
	ss = str(loginuser)
	split = ss.split('@' '')[0]
	try:
		img = User_Profile.objects.get(office_email=ss)
		print("img:=-----",img.profile_pic)
		if img.profile_pic == '':
			img = 'h' 
			imagedummy = 'h'
		else:
			print("---")
			img = User_Profile.objects.all().filter(office_email=ss)
			img = img
			imagedummy = 'h'
	except:
		img = User_Profile.objects.all().filter(office_email=ss)
		ss = len(img)
		if len(img) == 0:
			img = 'h'
			imagedummy = 'h'
	chahat = str(loginuser)
	all_datils = zip(ids_user,username_s)
	serchuser = Profile.objects.all()
	show_users_all = []
	for users in serchuser:
		show_users_all.append(users.first_name)
	loginuser = User.objects.get(username=request.user.username)
	if request.method == 'POST':
		new = request.POST['first-pass']
		olds = request.POST['middle-word']
		print(new,olds)
		if new == olds:
			print(new,olds)
			u = User.objects.get(username__exact=loginuser)
			print(u)
			u.set_password(new)
			u.save()
			chnge = 'Change Password Successfully'
			return render(request,'changepassword.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'image':imagedummy,'show_users':show_users_all,'chnge':chnge})
	return render(request,'changepassword.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'image':imagedummy,'show_users':show_users_all})
@login_required
def search_user(request):
	print("hit fun")
	today = date.today()
	match = str(today)
	update_obj = FileNote.objects.filter(file_note_date=today)
	lenth = []
	ids_user = []
	today_follow = []
	username_s = []
	bday = Profile.objects.all()
	ss = str(today)
	for brith in bday:
		try:
			if brith.dob[5:] == ss[5:]:
				if brith.last_name == None or brith.last_name == '':
					print(brith.first_name)
					lenth.append(brith.dob)
					username_ids = brith.first_name
					ids_user.append(username_ids)
					username_s.append('Birthday')
				else:
					lenth.append(brith.dob)
					username_id = str(brith.first_name)+' '+str(brith.last_name)
					ids_user.append(username_id)
					username_s.append('Birthday')
		except:
			pass
	for data in update_obj:
		lenth.append(data.file_note_date)
		ids_user.append(data.userid)
		nameusera = Profile.objects.get(userid=data.userid)
		username_ids = nameusera.last_name
		if username_ids == None:
			username_ids = nameusera.first_name
			username_s.append(username_ids)
		else:
			username_id = str(nameusera.first_name)+' '+str(nameusera.last_name)
			username_s.append(username_id)
		today_follow.append(data.file_note_date)
	if len(lenth) == 0:
		notify = 0
	else:
		notify = len(lenth)
	loginuser = User.objects.get(username=request.user.username)
	print("loginuser",loginuser)
	print("notify:",notify)
	ss = str(loginuser)
	split = ss.split('@' '')[0]
	try:
		img = User_Profile.objects.get(office_email=ss)
		print("img:=-----",img.profile_pic)
		if img.profile_pic == '':
			img = 'h' 
			imagedummy = 'h'
		else:
			print("---")
			img = User_Profile.objects.all().filter(office_email=ss)
			img = img
			imagedummy = 'h'
	except:
		img = User_Profile.objects.all().filter(office_email=ss)
		ss = len(img)
		if len(img) == 0:
			img = 'h'
			imagedummy = 'h'
	chahat = str(loginuser)
	all_datils = zip(ids_user,username_s)
	print(all_datils)
	
	serchuser = Profile.objects.all()
	print("serchuser:--",serchuser)
	show_users_all = []
	for users in serchuser:
		print(users.first_name)
		show_users_all.append(users.first_name)
	
	pre = []
	users = []
	user_names = []
	middle_names = []
	last_names = []
	dobs = []
	Emails = []
	contact_numbers = []
	Addresss = []
	correspondence_addresss = []
	Nationalitys = []
	Genders = []
	Marital_Statuss = []
	Country_Preference_as = []
	Country_Preference_bs = []
	Others_Countrys = []
	intakes = []
	final_user_list=[]
	if request.method =='POST':
		
		search = request.POST['search']
		try:
			print("hiiiiiii:---------",search.split(' ')[0])
			search = search.split(' ')[0]
		except:
			search = search
			print(search)

		if 'EDUAL' in search:
			details = Profile.objects.get(userid=search)
			prefix = details.prefix
			userids = details.userid
			username = details.first_name
			middle_name = details.middle_name
			last_name = details.last_name
			dob = details.dob
			Email = details.Email
			contact_number = details.contact_number
			Address = details.Address
			correspondence_address = details.correspondence_address
			Nationality = details.Nationality
			Gender = details.Gender
			Marital_Status = details.Marital_Status
			Country_Preference_a = details.Country_Preference_a
			Country_Preference_b = details.Country_Preference_b
			Others_Country = details.Others_Country
			intake = details.intake
			pre.append(prefix)
			users.append(userids)
			user_names.append(username)
			middle_names.append(middle_name)
			last_names.append(last_name)
			dobs.append(dob)
			Emails.append(Email)
			contact_numbers.append(contact_number)
			Addresss.append(Address)
			correspondence_addresss.append(correspondence_address)
			Nationalitys.append(Nationality)
			Genders.append(Gender)
			Marital_Statuss.append(Marital_Status)
			Country_Preference_as.append(Country_Preference_a)
			Country_Preference_bs.append(Country_Preference_b)
			Others_Countrys.append(Others_Country)
			intakes.append(intake)
			final_user_list = zip(users,pre,user_names,middle_names,last_names,dobs,Emails,contact_numbers,Addresss,correspondence_addresss,Nationalitys
				,Genders,Marital_Statuss,Country_Preference_as,Country_Preference_bs,Others_Countrys,intakes)
		else:
			detailss = Profile.objects.filter(first_name__icontains=search)
			print(detailss)
			if len(detailss) == 0:
				notfound = 'user not found'
				return render(request, 'user_not_found.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'notfound':notfound,'users':users,'show_users':show_users_all,'image':imagedummy,})
			else:
				for details in detailss:
					print(details.first_name)
					prefix = details.prefix
					userids = details.userid
					username = details.first_name
					middle_name = details.middle_name
					last_name = details.last_name
					dob = details.dob
					print("dob",dob)
					Email = details.Email
					contact_number = details.contact_number
					Address = details.Address
					correspondence_address = details.correspondence_address
					Nationality = details.Nationality
					Gender = details.Gender
					Marital_Status = details.Marital_Status
					Country_Preference_a = details.Country_Preference_a
					Country_Preference_b = details.Country_Preference_b
					Others_Country = details.Others_Country
					intake = details.intake
					pre.append(prefix)
					users.append(userids)
					user_names.append(username)
					middle_names.append(middle_name)
					last_names.append(last_name)
					dobs.append(dob)
					Emails.append(Email)
					contact_numbers.append(contact_number)
					Addresss.append(Address)
					correspondence_addresss.append(correspondence_address)
					Nationalitys.append(Nationality)
					Genders.append(Gender)
					Marital_Statuss.append(Marital_Status)
					Country_Preference_as.append(Country_Preference_a)
					Country_Preference_bs.append(Country_Preference_b)
					Others_Countrys.append(Others_Country)
					intakes.append(intake)
					final_user_list = zip(users,pre,user_names,middle_names,last_names,dobs,Emails,contact_numbers,Addresss,correspondence_addresss,Nationalitys
					,Genders,Marital_Statuss,Country_Preference_as,Country_Preference_bs,Others_Countrys,intakes)
	# final_user_list = ''
	# if 	final_user_list == '':
	# 	notfound = 'Please select the username or Id.'
	chahat = str(loginuser)
	if 'chahat@edulaunchers.com' in chahat:
		return render(request, 'loginhistory.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'final_urse_filer':final_user_list,'users':users,'show_users':show_users_all,'image':imagedummy})
	else:
		return render(request, 'edit.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'final_urse_filer':final_user_list,'users':users,'show_users':show_users_all,'image':imagedummy})
@login_required
def home_file(request):
	show_users_all = []
	db = Profile.objects.all()
	for sear in  db:
		show_users_all.append(sear.first_name)
	today = date.today()
	match = str(today)
	update_obj = FileNote.objects.filter(file_note_date=today)
	lenth = []
	ids_user = []
	today_follow = []
	username_s = []
	bday = Profile.objects.all()
	ss = str(today)
	for brith in bday:
		try:
			if brith.dob[5:] == ss[5:]:
				if brith.last_name == None or brith.last_name == '':
					print(brith.first_name)
					lenth.append(brith.dob)
					username_ids = brith.first_name
					ids_user.append(username_ids)
					username_s.append('Birthday')
				else:
					lenth.append(brith.dob)
					username_id = str(brith.first_name)+' '+str(brith.last_name)
					ids_user.append(username_id)
					username_s.append('Birthday')
		except:
			pass
	for data in update_obj:
		lenth.append(data.file_note_date)
		ids_user.append(data.userid)
		nameusera = Profile.objects.get(userid=data.userid)
		username_ids = nameusera.last_name
		if username_ids == None:
			username_ids = nameusera.first_name
			username_s.append(username_ids)
		else:
			username_id = str(nameusera.first_name)+' '+str(nameusera.last_name)
			username_s.append(username_id)
		today_follow.append(data.file_note_date)
	if len(lenth) == 0:
		notify = 0
	else:
		notify = len(lenth)
	loginuser = User.objects.get(username=request.user.username)
	ss = str(loginuser)
	split = ss.split('@' '')[0]
	try:
		img = User_Profile.objects.get(office_email=ss)
		if img.profile_pic == '':
			img = 'h' 
			imagedummy = 'h'
		else:
			print("---")
			img = User_Profile.objects.all().filter(office_email=ss)
			img = img
			imagedummy = 'h'
	except:
		img = User_Profile.objects.all().filter(office_email=ss)
		ss = len(img)
		if len(img) == 0:
			img = 'h'
			imagedummy = 'h'
	# last_month = datetime.now() - timedelta(days=7)
	# print(last_month)
	# data = (FileNote.objects.filter(date__date=last_month))
	data = FileNote.objects.all()
	print(len(data))
	result = reversed(data)
	print(result)
	user_weekid = []
	weekdate = []
	weekadvisor = []
	weeknote = []
	weekadd_file_datetime = []
	for week in result:
		user_weekid.append(week.userid)
		weekdate.append(week.date)
		weekadvisor.append(week.advisor)
		weeknote.append(week.note)
		weekadd_file_datetime.append(week.add_file_datetime)
	weekly = zip(user_weekid,weekadvisor,weeknote,weekadd_file_datetime)
	if request.method == 'POST':
		filetdate = request.POST['Follow']
		data = FileNote.objects.filter(date__date=filetdate)
		result = reversed(data)
		user_weekid = []
		weekdate = []
		weekadvisor = []
		weeknote = []
		weekadd_file_datetime = []
		for week in result:
			user_weekid.append(week.userid)
			weekdate.append(week.date)
			weekadvisor.append(week.advisor)
			weeknote.append(week.note)
			weekadd_file_datetime.append(week.add_file_datetime)
		weekly = zip(user_weekid,weekadvisor,weeknote,weekadd_file_datetime)
		all_datils = zip(ids_user,username_s)
		if len(user_weekid) == 0 and len(weekdate) == 0:
			record = 'Record not found'
		else:
			record = ''
		chahat = str(loginuser)
		if 'chahat@edulaunchers.com' in chahat:
			return render(request,'singledatfilter.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'weekly':weekly,'image':imagedummy,'show_users':show_users_all,'record':record,'date':filetdate})
		else:
			return render(request,'datefilter.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'weekly':weekly,'image':imagedummy,'show_users':show_users_all,'record':record,'date':filetdate})
	all_datils = zip(ids_user,username_s)
	chahat = str(loginuser)
	if 'chahat@edulaunchers.com' in chahat:
		print("dfsfsdfsdf")
		return render(request,'singleweekly.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'weekly':weekly,'image':imagedummy,'show_users':show_users_all})
	else:
		return render(request,'weekly.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'weekly':weekly,'image':imagedummy,'show_users':show_users_all})

@login_required
def home_demo(request):
	return render(request,'home_extend.html')
@login_required
def break_time(request):
	return render(request,'break.html')
@login_required
def answer_me(request):
	print("************")
	loginuser = User.objects.get(username=request.user.username)
	today = date.today()
	match = str(today)
	hostname = socket.gethostname()
	print('hostname:-----------------',loginuser)
	dates =  LoginHistory.objects.filter(ip=loginuser).last()
	user_input = request.GET.get('inputValue')
	print("LoginHistory:-------------",dates)
	if 'Start' in user_input:
		print("*****************",user_input)
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		print("Current Time =", current_time)
		dates.start_break = current_time
		dates.save()
	return render(request,'break.html')
@login_required
def answer(request):
	loginuser = User.objects.get(username=request.user.username)
	today = date.today()
	match = str(today)
	# hostname = socket.gethostname()
	# local_ip = socket.gethostbyname(hostname)
	print('hostname:loginuserloginuserloginuser-----------------',loginuser)
	dates =  LoginHistory.objects.filter(ip=loginuser).last()
	user_inputs = request.GET.get('inputValue')
	print("*------------",dates)
	if 'Stop' in user_inputs:
		print("//////////////////")
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		print("Current Time =", current_time)
		dates.stop_break = current_time
		dates.save()
	return render(request,'break.html')


@login_required
def local_usersss(request):
	serchuser = Profile.objects.all()
	show_users_all = []
	for users in serchuser:
		show_users_all.append(users.first_name)
	today = date.today()
	match = str(today)
	update_obj = FileNote.objects.filter(file_note_date=today)
	lenth = []
	ids_user = []
	today_follow = []
	username_s = []
	bday = Profile.objects.all()
	ss = str(today)
	for brith in bday:
		try:
			if brith.dob[5:] == ss[5:]:
				if brith.last_name == None or brith.last_name == '':
					print(brith.first_name)
					lenth.append(brith.dob)
					username_ids = brith.first_name
					ids_user.append(username_ids)
					username_s.append('Birthday')
				else:
					lenth.append(brith.dob)
					username_id = str(brith.first_name)+' '+str(brith.last_name)
					ids_user.append(username_id)
					username_s.append('Birthday')
		except:
			pass
	for data in update_obj:
		lenth.append(data.file_note_date)
		ids_user.append(data.userid)
		nameusera = Profile.objects.get(userid=data.userid)
		username_ids = nameusera.last_name
		if username_ids == None:
			username_ids = nameusera.first_name
			username_s.append(username_ids)
		else:
			username_id = str(nameusera.first_name)+' '+str(nameusera.last_name)
			username_s.append(username_id)
		today_follow.append(data.file_note_date)
	if len(lenth) == 0:
		notify = 0
	else:
		notify = len(lenth)
	loginuser = User.objects.get(username=request.user.username)
	ss = str(loginuser)
	split = ss.split('@' '')[0]
	try:
		img = User_Profile.objects.get(office_email=ss)
		print("img:=-----",img.profile_pic)
		if img.profile_pic == '':
			img = 'h' 
			imagedummy = 'h'
		else:
			print("---")
			img = User_Profile.objects.all().filter(office_email=ss)
			img = img
			imagedummy = 'h'
	except:
		img = User_Profile.objects.all().filter(office_email=ss)
		ss = len(img)
		if len(img) == 0:
			img = 'h'
			imagedummy = 'h'
	users_email = []
	users_no = []		
	users_datas = User_Profile.objects.all()
	for dta in users_datas:
		users_email.append(dta.office_email)
		users_no.append(dta.contact_number)
	users_data = zip(users_email,users_no)
	all_datils = zip(ids_user,username_s)
	return render(request,'userinfo.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'user':users_data,'image':imagedummy,'show_users':show_users_all})
@login_required
def homepage(request):
	today = date.today()
	update_obj = FileNote.objects.filter(file_note_date=today)
	lenth = []
	ids_user = []
	today_follow = []
	username_s = []
	bday = Profile.objects.all()
	ss = str(today)
	for brith in bday:
		try:
			if brith.dob[5:] == ss[5:]:
				if brith.last_name == None or brith.last_name == '':
					print(brith.first_name)
					lenth.append(brith.dob)
					username_ids = brith.first_name
					ids_user.append(username_ids)
					username_s.append('Birthday')
				else:
					lenth.append(brith.dob)
					username_id = str(brith.first_name)+' '+str(brith.last_name)
					ids_user.append(username_id)
					username_s.append('Birthday')
		except:
			pass
	for data in update_obj:
		lenth.append(data.file_note_date)
		ids_user.append(data.userid)
		nameusera = Profile.objects.get(userid=data.userid)
		# try:
		username_ids = nameusera.last_name
		if username_ids == None:
			username_ids = nameusera.first_name
			username_s.append(username_ids)
		else:
			username_id = str(nameusera.first_name)+' '+str(nameusera.last_name)
			username_s.append(username_id)
		# except:
		# 	pass
		# today_follow.append(data.file_note_date)
	print()
	if len(lenth) == 0:
		notify = 0
	else:
		notify = len(lenth)
	loginuser = User.objects.get(username=request.user.username)
	ss = str(loginuser)
	split = ss.split('@' '')[0]
	

	try:
		img = User_Profile.objects.get(office_email=ss)
		if img.profile_pic == '':
			img = 'h' 
			imagedummy = 'h'
		else:
			print("---")
			img = User_Profile.objects.all().filter(office_email=ss)
			img = img
			imagedummy = 'h'
	except:
		img = User_Profile.objects.all().filter(office_email=ss)
		ss = len(img)
		if len(img) == 0:
			img = 'h'
			imagedummy = 'h'
	
	
	all_datils = zip(ids_user,username_s)
	serchuser = Profile.objects.all()
	show_users_all = []
	for users in serchuser:
		show_users_all.append(users.first_name)
	chahat = str(loginuser)
	total_leads = []
	total_Inqu = []
	offers = []
	for i in serchuser:
		if i.inquiry_status == 'Lead':
			total_leads.append(i.inquiry_status)
		if i.inquiry_status == 'Hot' or i.inquiry_status == 'Cold' or i.inquiry_status == 'Warm' or i.inquiry_status == 'Hot ':
			total_Inqu.append(i.inquiry_status)
		if i.inquiry_status == 'Offer accepted':
			print(i.inquiry_status)
			offers.append(i.inquiry_status)
	
	
	led = len(total_leads)
	inq = len(total_Inqu)
	offerssss = len(offers)
	if chahat == 'chahat@edulaunchers.com':
		print("fdsfdfds")
		return render(request,'logs.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'image':imagedummy,'show_users':show_users_all,'inq':inq,'led':led,'offerssss':offerssss})
	else:		
		return render(request,'homepage.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'image':imagedummy,'show_users':show_users_all,'inq':inq,'led':led,'offerssss':offerssss})


class ChartData(APIView):
	def get(self,request,format=None):
		
		month = Profile.objects.all()
		monhts = []
		for filters in month:
			monhts.append(filters.month)
		
		from collections import Counter
		d = Counter(monhts)
		list_of_month = []
		value_of_month = []
		checks = []
		import calendar
		for x in range(1,13):
			if x == 1:
				for key, value in d.items():
					if key == 'January':
						list_of_month.append('January')
						value_of_month.append(value)
					else:
						i = 'January'
						if i not in list_of_month:
							list_of_month.append(i)
						
						j = 0
						if j not in value_of_month:
							value_of_month.append(j)
			if x == 2:
				for key, value in d.items():
					if key == 'February':
						list_of_month.append('February')
						value_of_month.append(value)
					else:
						i = 'February'
						if i not in list_of_month:
							list_of_month.append(i)
						j = '0'
						if j not in value_of_month:
							value_of_month.append(j)	
			if x == 3:
				for key, value in d.items():
					if key == 'March':
						list_of_month.append('March')
						value_of_month.append(value)
					else:
						i = 'March'
						if i not in list_of_month:
							list_of_month.append(i)
						j = '00'
						if j not in value_of_month:
							value_of_month.append(j)
			if x == 4:
				for key, value in d.items():
					if key == 'April':
						list_of_month.append('April')
						value_of_month.append(value)
					else:
						i = 'April'
						if i not in list_of_month:
							list_of_month.append(i)
						j = '000'
						if j not in value_of_month:
							value_of_month.append(j)
			if x == 5:
				for key, value in d.items():
					if key == 'May':
						list_of_month.append('May')
						value_of_month.append(value)

			if x == 6:
				for key, value in d.items():
					if key == 'June':
						list_of_month.append('June')
						value_of_month.append(value)
					
			
			if x == 7:
				for key, value in d.items():
					if key == 'July':
						if value != '':
							list_of_month.append('July')
							value_of_month.append(value)
							break
					
			if x == 8:
				for key, value in d.items():
					if key == 'August':
						if value != '':
							list_of_month.append('August')
							value_of_month.append(value)
							break
					
			if x == 9:
				for key, value in d.items():
					if key == 'September':
						if value != '':
							list_of_month.append('September')
							value_of_month.append(value)
							break
					# else:
					# 	i = 'September'
					# 	if i not in list_of_month:
					# 		list_of_month.append(i)
					# 	j = '00000'
					# 	if j not in value_of_month:
					# 		value_of_month.append(j)
			if x == 10:
				for key, value in d.items():
					if key == 'October':
						list_of_month.append('October')
						value_of_month.append(value)
					else:
						i = 'October'
						if i not in list_of_month:
							list_of_month.append(i)
						j = '000000'
						if j not in value_of_month:
							value_of_month.append(j)
			if x == 11:
				for key, value in d.items():
					if key == 'November':
						list_of_month.append('November')
						value_of_month.append(value)
					else:
						i = 'November'
						if i not in list_of_month:
							list_of_month.append(i)
						j = '0000000'
						if j not in value_of_month:
							value_of_month.append(j)
			if x == 12:
				for key, value in d.items():
					if key == 'December':
						list_of_month.append('December')
						value_of_month.append(value)
					else:
						i = 'December'
						if i not in list_of_month:
							list_of_month.append(i)
						j = '00000000'
						if j not in value_of_month:
							value_of_month.append(j)

		labels= list_of_month
		chartLabel = "Leads"
		chartdata = value_of_month
		data={
					 "labels":labels,
					 "chartLabel":chartLabel,
					 "chartdata":chartdata,
			 }

		

		return Response(data)

@login_required
def User_Profiles(request):
	loginuser = User.objects.get(username=request.user.username)
	listofuserv =[]
	all_u = User_Profile.objects.all()
	for data in all_u:
		listofuserv.append(data.office_email)
	if  str(loginuser) in listofuserv:
		pass
	else:	
		obj = User_Profile(office_email=loginuser,last_name=None,name=None,Email=None,contact_number=None,profile_pic=None)
		obj.save()
	try:
		userv= User_Profile.objects.get(office_email=loginuser)
		dd = userv.profile_pic
		names = userv.name
		last_name = userv.last_name
		Emails = userv.Email
		contact_number = userv.contact_number
		
	except:
		pass
	if request.method == 'POST':
		try:
			pic = request.FILES['myfile']
			if dd == 'None' or dd == None:
				pic = request.FILES['myfile']
				if pic != '':
					userv.profile_pic = pic
					userv.save()
			else:
				pic = request.FILES['myfile']
				userv.profile_pic = pic
				userv.save()
		except:
			pass
		
		try:
			if names == None:
				first = request.POST['first-name']
				if first != '':
					userv.name = first
					userv.save()
				else:
					pass
			else:
				first = names
				userv.name = first
				userv.save()
		except:
			first = None
			userv.name = first
			userv.save()
		try:
			if last_name == None or last_name == 'None':
				last = request.POST['Last-name']
				if last != '':
					userv.last_name = last
					userv.save()
			else:
				last = last_name
				userv.last_name = last
				userv.save()
		except:
			last_name = None
			userv.last_name = last_name
			userv.save()
		try:
			if Emails == None:
				email = request.POST['email']
				if email != '':
					userv.Email = email
					userv.save()
				else:
					pass
			else:
				email = Emails
				userv.Email = email
				userv.save()
		except:
			email = None
			userv.Email = email
			userv.save()
		try:
			if contact_number == None or contact_number == 'None':
				umber = request.POST['number']
				if umber != '':
					userv.contact_number = umber
					userv.save()
			else:
				umber = contact_number
				userv.contact_number = umber
				userv.save()
		except:
			contact_number = None
			userv.contact_number = contact_number
			userv.save()
		return HttpResponseRedirect('/user_profile/')
	today = date.today()
	match = str(today)
	update_obj = FileNote.objects.filter(file_note_date=today)
	lenth = []
	ids_user = []
	today_follow = []
	username_s = []
	bday = Profile.objects.all()
	ss = str(today)
	for brith in bday:
		try:
			if brith.dob[5:] == ss[5:]:
				if brith.last_name == None or brith.last_name == '':
					print(brith.first_name)
					lenth.append(brith.dob)
					username_ids = brith.first_name
					ids_user.append(username_ids)
					username_s.append('Birthday')
				else:
					lenth.append(brith.dob)
					username_id = str(brith.first_name)+' '+str(brith.last_name)
					ids_user.append(username_id)
					username_s.append('Birthday')
		except:
			pass
	for data in update_obj:
		# if match == data.next_followup_notification:
		lenth.append(data.file_note_date)
		ids_user.append(data.userid)
		nameusera = Profile.objects.get(userid=data.userid)
		username_ids = nameusera.last_name
		if username_ids == None:
			username_ids = nameusera.first_name
			username_s.append(username_ids)
		else:
			username_id = str(nameusera.first_name)+' '+str(nameusera.last_name)
			username_s.append(username_id)
		today_follow.append(data.file_note_date)
	if len(lenth) == 0:
		notify = 0
	else:
		notify = len(lenth)

	loginuser = User.objects.get(username=request.user.username)
	print("loginuser",loginuser)
	print("notify:",notify)
	ss = str(loginuser)
	split = ss.split('@' '')[0]
	try:
		img = User_Profile.objects.get(office_email=ss)
		print("img:=-----",img.profile_pic)
		if img.profile_pic == '':
			img = 'h' 
			imagedummy = 'h'
		else:
			print("---")
			img = User_Profile.objects.all().filter(office_email=ss)
			img = img
			imagedummy = 'h'
	except:
		img = User_Profile.objects.all().filter(office_email=ss)
		ss = len(img)
		if len(img) == 0:
			img = 'h'
			imagedummy = 'h'
	chahat = str(loginuser)
	all_datils = zip(ids_user,username_s)
	serchuser = Profile.objects.all()
	print("serchuser:--",serchuser)
	show_users_all = []
	for users in serchuser:
		show_users_all.append(users.first_name)
	if 'chahat@edulaunchers.com' in chahat:
		return render(request,'profile1.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'image':imagedummy,'show_users':show_users_all,'dd':dd,'names':names,'last_name':last_name,
		'Emails':Emails,'contact_number':contact_number})
	else:
		return render(request,'profile.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'image':imagedummy,'show_users':show_users_all,'dd':dd,'names':names,'last_name':last_name,
		'Emails':Emails,'contact_number':contact_number})

@login_required
def User_Profiless(request):
	loginuser = User.objects.get(username=request.user.username)
	try:
		userv= User_Profile.objects.get(office_email=loginuser)
		dd = userv.profile_pic
		names = userv.name
		last_name = userv.last_name
		Emails = userv.Email
		contact_number = userv.contact_number
		
	except:
		pass
	if request.method == 'POST':
		try:
			pic = request.FILES['myfile']
			if dd == 'None' or dd == None:
				pic = request.FILES['myfile']
				if pic != '':
					userv.profile_pic = pic
					userv.save()
			else:
				pic = request.FILES['myfile']
				userv.profile_pic = pic
				userv.save()
		except:
			pass
		
		try:
			first = request.POST['first-name']
			if first != '':
				userv.name = first
				userv.save()
			else:
				pass
		except:
			pass
		try:
			last = request.POST['Last-name']
			if last != '':
				userv.last_name = last
				userv.save()
		except:
			pass
		try:
			email = request.POST['email']
			if email != '':
				userv.Email = email
				userv.save()
			else:
				pass
		except:
			pass
		try:
			umber = request.POST['number']
			if umber != '':
				userv.contact_number = umber
				userv.save()
		except:
			pass
		return HttpResponseRedirect('/user_profile/')
	today = date.today()
	match = str(today)
	update_obj = FileNote.objects.filter(file_note_date=today)
	lenth = []
	ids_user = []
	today_follow = []
	username_s = []
	bday = Profile.objects.all()
	ss = str(today)
	for brith in bday:
		try:
			if brith.dob[5:] == ss[5:]:
				if brith.last_name == None or brith.last_name == '':
					print(brith.first_name)
					lenth.append(brith.dob)
					username_ids = brith.first_name
					ids_user.append(username_ids)
					username_s.append('Birthday')
				else:
					lenth.append(brith.dob)
					username_id = str(brith.first_name)+' '+str(brith.last_name)
					ids_user.append(username_id)
					username_s.append('Birthday')
		except:
			pass
	for data in update_obj:
		# if match == data.next_followup_notification:
		lenth.append(data.file_note_date)
		ids_user.append(data.userid)
		nameusera = Profile.objects.get(userid=data.userid)
		username_ids = nameusera.last_name
		if username_ids == None:
			username_ids = nameusera.first_name
			username_s.append(username_ids)
		else:
			username_id = str(nameusera.first_name)+' '+str(nameusera.last_name)
			username_s.append(username_id)
		today_follow.append(data.file_note_date)
	if len(lenth) == 0:
		notify = 0
	else:
		notify = len(lenth)

	print("loginuser",loginuser)
	print("notify:",notify)
	ss = str(loginuser)
	split = ss.split('@' '')[0]
	try:
		img = User_Profile.objects.get(office_email=ss)
		print("img:=-----",img.profile_pic)
		if img.profile_pic == '':
			img = 'h' 
			imagedummy = 'h'
		else:
			print("---")
			img = User_Profile.objects.all().filter(office_email=ss)
			img = img
			imagedummy = 'h'
	except:
		img = User_Profile.objects.all().filter(office_email=ss)
		ss = len(img)
		if len(img) == 0:
			img = 'h'
			imagedummy = 'h'
	chahat = str(loginuser)
	all_datils = zip(ids_user,username_s)
	
	serchuser = Profile.objects.all()
	print("serchuser:--",serchuser)
	show_users_all = []
	for users in serchuser:
		show_users_all.append(users.first_name)
	if 'chahat@edulaunchers.com' in chahat:
		return render(request,'image1.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'image':imagedummy,'show_users':show_users_all,'dd':dd,'names':names,'last_name':last_name,
		'Emails':Emails,'contact_number':contact_number})
	else:
		return render(request,'image.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'image':imagedummy,'show_users':show_users_all,'dd':dd,'names':names,'last_name':last_name,
		'Emails':Emails,'contact_number':contact_number})
def login_user(request):
	if request.method == 'POST':
		username = request.POST.get('js')
		password = request.POST.get('aak')
		print(username,password)
		user  = authenticate(username=username.lower(), password=password)
		if user:
			if user.is_active:
				# request.session.set_expiry(90000000)
				login(request, user)
				loginuser = User.objects.get(username=request.user.username)
				from datetime import datetime
				now = datetime.now()
				current_time = now.strftime("%H:%M:%S")
				obj = LoginHistory.objects.create(user =  User.objects.get(username=loginuser),login_time = current_time,ip=loginuser)
				return HttpResponseRedirect('/mainpage/')
		else:
			wrong = 'Please enter the correct email and password'
			return render(request, 'signin.html',{'pass':wrong})
	return render(request, 'signin.html')
@login_required
def all_user_logs(request):
	return render(request,'testlogs.html')
@login_required
def admin_page(request):
	today = date.today()
	match = str(today)
	update_obj = FileNote.objects.filter(file_note_date=today)
	lenth = []
	ids_user = []
	today_follow = []
	username_s = []
	bday = Profile.objects.all()
	ss = str(today)
	for brith in bday:
		try:
			if brith.dob[5:] == ss[5:]:
				if brith.last_name == None or brith.last_name == '':
					print(brith.first_name)
					lenth.append(brith.dob)
					username_ids = brith.first_name
					ids_user.append(username_ids)
					username_s.append('Birthday')
				else:
					lenth.append(brith.dob)
					username_id = str(brith.first_name)+' '+str(brith.last_name)
					ids_user.append(username_id)
					username_s.append('Birthday')
		except:
			pass
	for data in update_obj:
		lenth.append(data.file_note_date)
		ids_user.append(data.userid)
		nameusera = Profile.objects.get(userid=data.userid)
		username_ids = nameusera.last_name
		if username_ids == None:
			username_ids = nameusera.first_name
			username_s.append(username_ids)
		else:
			username_id = str(nameusera.first_name)+' '+str(nameusera.last_name)
			username_s.append(username_id)
		today_follow.append(data.file_note_date)
	if len(lenth) == 0:
		notify = 0
	else:
		notify = len(lenth)
	loginuser = User.objects.get(username=request.user.username)
	ss = str(loginuser)
	split = ss.split('@' '')[0]
	try:
		img = User_Profile.objects.get(office_email=ss)
		if img.profile_pic == '':
			img = 'h' 
			imagedummy = 'h'
		else:
			print("---")
			img = User_Profile.objects.all().filter(office_email=ss)
			img = img
			imagedummy = 'h'
	except:
		img = User_Profile.objects.all().filter(office_email=ss)
		ss = len(img)
		if len(img) == 0:
			img = 'h'
			imagedummy = 'h'
	
	all_datils = zip(ids_user,username_s)
	
	serchuser = Profile.objects.all()
	show_users_all = []
	for users in serchuser:
		show_users_all.append(users.first_name)
	if request.method == 'GET':
		users = LoginHistory.objects.all().order_by('created_at')

		username_user = []
		dates_time = []
		time_logins = []
		logout_times = []
		start_breaks = []
		stop_breaks = []
		result = reversed(users)
		for user_data in result:
			sp = user_data.user
			split = str(sp).split('@' '')[0]
			print("sp:-------------",split)
			username_user.append(split)
			dates_time.append(user_data.created_at)
			time_logins.append(user_data.login_time)
			if user_data.logout_time == None or user_data.logout_time == 'None':
				logout_times.append('')
			else:
				logout_times.append(user_data.logout_time)
			if user_data.start_break == None:
				start_breaks.append('')
			else:
				start_breaks.append(user_data.start_break)
			if user_data.stop_break == None:
				stop_breaks.append('')
			else:
				stop_breaks.append(user_data.stop_break)
	user = zip(username_user,dates_time,time_logins,logout_times,start_breaks,stop_breaks)
	return render(request, 'logtoday.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'image':imagedummy,'show_users':show_users_all,'username':user})
@login_required
def logout_view(request):
	# hostname = socket.gethostname()
	# local_ip = socket.gethostbyname(hostname)
	loginuser = User.objects.get(username=request.user.username)
	sss = LoginHistory.objects.filter(ip=loginuser)
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	for ssss in sss:
		if ssss.logout_time == None or ssss.logout_time == 'None':
			ssss.logout_time = current_time
			ssss.save()
	logout(request)
	return HttpResponseRedirect('/')
@login_required
def registerpage(request):
	profileId = request.GET.get('info')
	loginuser = User.objects.get(username=request.user.username)
	userinfo = Profile.objects.get(userid=profileId)
	inquiry_status = userinfo.inquiry_status
	print(inquiry_status)
	reference = userinfo.reference
	prefix = userinfo.prefix
	first_name = userinfo.first_name
	middle_name = userinfo.middle_name
	last_name = userinfo.last_name
	dob = userinfo.dob
	Email = userinfo.Email
	contact_number = userinfo.contact_number
	Address = userinfo.Address
	_address = userinfo.correspondence_address
	Nationality = userinfo.Nationality
	Gender = userinfo.Gender
	Marital_Status = userinfo.Marital_Status
	Preference_a = userinfo.Country_Preference_a
	Preference_b = userinfo.Country_Preference_b
	Others_Country = userinfo.Others_Country
	intake = userinfo.intake
	if request.method == 'POST':
		profileId = request.GET.get('info')
		print('data:---',profileId)
		update_obj = Profile.objects.get(userid=profileId)
		try:
			inq = request.POST['iinq']
			print('inq',inq)
		except:
			inq = ''
		try:
			Prefixss = request.POST['Prefixs']
			print('Prefixss',Prefixss)
		except:
			Prefixss = ''
		# f_name = request.POST['first-name']
		# m_name = request.POST['middle-name']
		# l_name = request.POST['Last-name']
		# dobs = request.POST['birthday']

		try:
			f_name = request.POST['first-name']
		except:
			f_name = ''
		try:
			m_name = request.POST['middle-name']
		except:
			m_name = ''
		try:
			l_name = request.POST['Last-name']
		except:
			l_name = ''
		try:
			birthdays = request.POST['birthday']
			print("dobs",birthdays)
		except:
			birthdays = ''
		try:
			emails = request.POST['email']
		except:
			emails = ''
		try:
			numbers = request.POST['number']
		except:
			numbers = ''
		try:
			Genderss = request.POST['Genders']
		except:
			Genderss = ''
		try:
			Statusa = request.POST['Status']
		except:
			Statusa = ''
		try:
			Nationalit = request.POST['Nationalitys']
		except:
			Nationalit = ''
		try:
			homeaddresssss = request.POST['homeaddresss']
		except:
			homeaddresssss = ''
		try:
			titles = request.POST['title']
		except:
			titles = ''
		try:
			countryAs = request.POST['countryA']
		except:
			countryAs = ''
		try:
			countrybs = request.POST['countryB']
		except:
			countrybs = ''
		try:
			Othersss = request.POST['Otherss']
		except:
			Othersss = ''
		try:
			Intakestarts = request.POST['Intakestart']
		except:
			Intakestarts = ''
		
		update_obj.inquiry_status = inq
		update_obj.prefix= Prefixss
		update_obj.first_name= f_name
		update_obj.middle_name= m_name
		update_obj.last_name= l_name
		update_obj.dob= birthdays
		update_obj.Email= emails
		update_obj.contact_number=numbers
		update_obj.Address=homeaddresssss
		update_obj.correspondence_address=titles
		update_obj.Nationality=Nationalit
		update_obj.Gender=Genderss
		update_obj.Marital_Status=Statusa
		update_obj.Country_Preference_a=countryAs
		update_obj.Country_Preference_b=countrybs
		update_obj.Others_Country=Othersss
		update_obj.intake=Intakestarts
		update_obj.save()
	users = str(loginuser)
	today = date.today()
	match = str(today)
	update_obj = FileNote.objects.filter(file_note_date=today)
	lenth = []
	ids_user = []
	today_follow = []
	username_s = []
	bday = Profile.objects.all()
	ss = str(today)
	for brith in bday:
		try:
			if brith.dob[5:] == ss[5:]:
				if brith.last_name == None or brith.last_name == '':
					print(brith.first_name)
					lenth.append(brith.dob)
					username_ids = brith.first_name
					ids_user.append(username_ids)
					username_s.append('Birthday')
				else:
					lenth.append(brith.dob)
					username_id = str(brith.first_name)+' '+str(brith.last_name)
					ids_user.append(username_id)
					username_s.append('Birthday')
		except:
			pass
	for data in update_obj:
		# if match == data.next_followup_notification:
		lenth.append(data.file_note_date)
		ids_user.append(data.userid)
		nameusera = Profile.objects.get(userid=data.userid)
		username_ids = nameusera.last_name
		if username_ids == None:
			username_ids = nameusera.first_name
			username_s.append(username_ids)
		else:
			username_id = str(nameusera.first_name)+' '+str(nameusera.last_name)
			username_s.append(username_id)
		today_follow.append(data.file_note_date)
	if len(lenth) == 0:
		notify = 0
	else:
		notify = len(lenth)

	loginuser = User.objects.get(username=request.user.username)
	print("loginuser",loginuser)
	print("notify:",notify)
	ss = str(loginuser)
	split = ss.split('@' '')[0]
	try:
		img = User_Profile.objects.get(office_email=ss)
		print("img:=-----",img.profile_pic)
		if img.profile_pic == '':
			img = 'h' 
			imagedummy = 'h'
		else:
			print("---")
			img = User_Profile.objects.all().filter(office_email=ss)
			img = img
			imagedummy = 'h'
	except:
		img = User_Profile.objects.all().filter(office_email=ss)
		ss = len(img)
		if len(img) == 0:
			img = 'h'
			imagedummy = 'h'
	serchuser = Profile.objects.all()
	print("serchuser:--",serchuser)
	show_users_all = []
	for use in serchuser:
		show_users_all.append(use.first_name)
	chahat = str(loginuser)
	all_datils = zip(ids_user,username_s)
	if first_name != '' and contact_number != '':
		do = 'Information saved successfully'
	else:
		do = ''
	if 'chahat@edulaunchers.com' in users:
		return render(request, 'editregister.html',{'inquiry_status':inquiry_status,'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'profileId':profileId,'reference':reference,'prefix':prefix,'first_name':first_name,'middle_name':middle_name,
		'last_name':last_name,'dob':dob,'Email':Email,'contact_number':contact_number,'Address':Address,'address':_address,'Nationality':Nationality,
		'Gender':Gender,'Marital_Status':Marital_Status,'Preference_a':Preference_a,'Preference_b':Preference_b,'Others_Country':Others_Country,'intake':intake,'do':do})
	else:
		return render(request, 'registeredit.html',{'inquiry_status':inquiry_status,'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'profileId':profileId,'reference':reference,'prefix':prefix,'first_name':first_name,'middle_name':middle_name,
		'last_name':last_name,'dob':dob,'Email':Email,'contact_number':contact_number,'Address':Address,'address':_address,'Nationality':Nationality,
		'Gender':Gender,'Marital_Status':Marital_Status,'Preference_a':Preference_a,'Preference_b':Preference_b,'Others_Country':Others_Country,'intake':intake,'image':imagedummy,'show_users':show_users_all,'do':do})
@login_required
def signup(request):
	today = date.today()
	
	serchuser = Profile.objects.all()
	show_users_all = []
	for users in serchuser:
		show_users_all.append(users.first_name)
	loginuser = User.objects.get(username=request.user.username)
	if request.method == 'POST':
		month_number = str(today)
		month_numbers = month_number.split('-' '')[1]
		datetime_object = datetime.strptime(month_numbers, "%m")
		month_name = datetime_object.strftime("%B")
		try:
			last = idinfo.objects.last()
			ids = last.userid
			if ids == 'EDUAL0':
				data = ids.split('L')[1]
				id_ = int(data) + 1
				final = 'EDUAL'+ str(id_)
				emp = idinfo.objects.all()
				emp.delete()
		except:
			last = Profile.objects.latest("datetime")
			ids = last.userid
			data = ids.split('L')[1]
			id_ = int(data) + 1
			final = 'EDUAL'+ str(id_)
		try:
			status = request.POST['statuss']
		except:
			status = ''

		Prefixs = request.POST['Prefixs']
		print('status:----------',status)
		firstname = request.POST['first-name']
		middlename = request.POST['middle-name']
		Lastname = request.POST['Last-name']
		birthdays = request.POST['birthday']
		emails = request.POST['email']
		mobile  = request.POST['number']
		leadSSS  = request.POST['leads']
		if leadSSS == 'Reference':
			leadSSS  = request.POST['ref_name']
		else:
			leadSSS  = leadSSS
		Address  = request.POST['homeaddresss']
		CorrAddress  = request.POST['title']
		Nationality  = request.POST['Nationalitys']
		Genders = request.POST['Genders']
		print('Genders:----------',Genders)
		MaritalStatus = request.POST['Status']
		countryA = request.POST['countryA']
		countryB = request.POST['countryB']
		Otherscountry = request.POST['Otherss']
		Intake = request.POST['Intakestart']
		info = Profile(advisor=str(loginuser),inquiry_status=status,userid=final,reference=leadSSS,prefix=Prefixs,first_name=firstname,middle_name=middlename,last_name=Lastname,dob=birthdays,Email=emails,contact_number=mobile,
		Address=Address,correspondence_address=CorrAddress,Nationality=Nationality,Gender=Genders,Marital_Status=MaritalStatus,Country_Preference_a=countryA,
		Country_Preference_b=countryB,Others_Country=Otherscountry,intake=Intake,month=month_name)
		info.save()
		return redirect('/editfinfo/?info='+str(final))
	try:
		last = idinfo.objects.last()
		ids = last.userid
		if ids == 'EDUAL0':
			data = ids.split('L')[1]
			id_ = int(data) + 1
			final = 'EDUAL'+ str(id_)			
	except:
		last = Profile.objects.latest("datetime")
		ids = last.userid
		data = ids.split('L')[1]
		id_ = int(data) + 1
		final = 'EDUAL'+ str(id_)
	county = country.objects.all()
	today = date.today()
	match = str(today)
	update_obj = FileNote.objects.filter(file_note_date=today)
	lenth = []
	ids_user = []
	today_follow = []
	username_s = []
	bday = Profile.objects.all()
	ss = str(today)
	for brith in bday:
		try:
			if brith.dob[5:] == ss[5:]:
				if brith.last_name == None or brith.last_name == '':
					print(brith.first_name)
					lenth.append(brith.dob)
					username_ids = brith.first_name
					ids_user.append(username_ids)
					username_s.append('Birthday')
				else:
					lenth.append(brith.dob)
					username_id = str(brith.first_name)+' '+str(brith.last_name)
					ids_user.append(username_id)
					username_s.append('Birthday')
		except:
			pass
	for data in update_obj:
		# if match == data.next_followup_notification:
		lenth.append(data.file_note_date)
		ids_user.append(data.userid)
		nameusera = Profile.objects.get(userid=data.userid)
		username_ids = nameusera.last_name
		if username_ids == None:
			username_ids = nameusera.first_name
			username_s.append(username_ids)
		else:
			username_id = str(nameusera.first_name)+' '+str(nameusera.last_name)
			username_s.append(username_id)
		today_follow.append(data.file_note_date)
	if len(lenth) == 0:
		notify = 0
	else:
		notify = len(lenth)

	loginuser = User.objects.get(username=request.user.username)
	print("loginuser",loginuser)
	print("notify:",notify)
	ss = str(loginuser)
	split = ss.split('@' '')[0]
	try:
		img = User_Profile.objects.get(office_email=ss)
		print("img:=-----",img.profile_pic)
		if img.profile_pic == '':
			img = 'h' 
			imagedummy = 'h'
		else:
			print("---")
			img = User_Profile.objects.all().filter(office_email=ss)
			img = img
			imagedummy = 'h'
	except:
		img = User_Profile.objects.all().filter(office_email=ss)
		ss = len(img)
		if len(img) == 0:
			img = 'h'
			imagedummy = 'h'
	all_datils = zip(ids_user,username_s)
	users = str(loginuser)
	if 'chahat@edulaunchers.com' in users:
		print("dfsdfsdf")
		return render(request, 'register1.html',{'hotel_images' : img,'notify':notify,'all_datils':all_datils,'userid':final,'county':county,'loginuser':loginuser,'image':imagedummy,'show_users':show_users_all})
	else:
		return render(request, 'register.html',{'hotel_images' : img,'notify':notify,'all_datils':all_datils,'userid':final,'county':county,'loginuser':loginuser,'image':imagedummy,'show_users':show_users_all})
@login_required
def followsametime(request):
	loginuser = User.objects.get(username=request.user.username)
	follow = request.GET.get('final')
	print("follow",follow)
	if request.method =='POST':
		print("sdfsdf")
		Comments_follow_up = request.POST['Comments']
		# next_follow_date = request.POST['Follow']
		obj = Followup.objects.create(
		userid =  Profile.objects.get(userid=follow),
		advisor = loginuser,
		last_follow_up_text = Comments_follow_up)
		return redirect('/user/')
	users = str(loginuser)
	today = date.today()
	print(today)
	match = str(today)
	update_obj = Followup.objects.all()
	lenth = []
	ids_user = []
	today_follow = []
	username_s = []
	bday = Profile.objects.all()
	ss = str(today)
	for brith in bday:
		try:
			if brith.dob[5:] == ss[5:]:
				if brith.last_name == None or brith.last_name == '':
					print(brith.first_name)
					lenth.append(brith.dob)
					username_ids = brith.first_name
					ids_user.append(username_ids)
					username_s.append('Birthday')
				else:
					lenth.append(brith.dob)
					username_id = str(brith.first_name)+' '+str(brith.last_name)
					ids_user.append(username_id)
					username_s.append('Birthday')
		except:
			pass
	for data in update_obj:
		if match == data.next_followup_notification:
			lenth.append(data.next_followup_notification)
			ids_user.append(data.userid)
			nameusera = Profile.objects.get(userid=data.userid)
			username_ids = nameusera.last_name
			if username_ids == None:
				username_ids = nameusera.first_name
				username_s.append(username_ids)
			else:
				username_id = str(nameusera.first_name)+' '+str(nameusera.last_name)
				username_s.append(username_id)
			today_follow.append(data.next_followup_notification)
	if len(lenth) == 0:
		notify = 0
	else:
		notify = len(lenth)
	loginuser = User.objects.get(username=request.user.username)
	print("loginuser",loginuser)
	print("notify:",notify)
	ss = str(loginuser)
	split = ss.split('@' '')[0]
	try:
		img = User_Profile.objects.get(office_email=ss)
		print("img:=-----",img.profile_pic)
		if img.profile_pic == '':
			img = 'h' 
			imagedummy = 'h'
		else:
			print("---")
			img = User_Profile.objects.all().filter(office_email=ss)
			img = img
			imagedummy = 'h'
	except:
		img = User_Profile.objects.all().filter(office_email=ss)
		ss = len(img)
		if len(img) == 0:
			img = 'h'
			imagedummy = 'h'
	chahat = str(loginuser)
	all_datils = zip(ids_user,username_s)
	serchuser = Profile.objects.all()
	print("serchuser:--",serchuser)
	show_users_all = []
	for usersssss in serchuser:
		print("*************************",usersssss.first_name)
		show_users_all.append(usersssss.first_name)

	if 'chahat@edulaunchers.com' in users:
		print("dfsdfsdf")
		return render(request,'follows1.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'follows':follow})
	else:
		return render(request,'follows.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'follows':follow,'image':imagedummy,'show_users':show_users_all})
x = ''
@login_required
def file_notes(request):
	loginuser = User.objects.get(username=request.user.username)
	file_note = request.GET.get('file')
	import datetime
	now = datetime.datetime.now()
	today_date = now.strftime("%Y-%m-%d %H:%M:%S")
	if request.method =='POST':
		note_file = request.POST['datas']
		notes_date = request.POST['notes']
		global x
		x = "fantastic"
		obj = FileNote.objects.create(
		userid =  Profile.objects.get(userid=file_note),
		note = note_file,
		advisor = loginuser,
		file_note_date=notes_date,
		add_file_datetime=today_date)
		return redirect('/note/?file='+str(file_note))
	
	users = str(loginuser)
	today = date.today()
	update_obj = FileNote.objects.filter(file_note_date=today)
	lenth = []
	ids_user = []
	today_follow = []
	username_s = []
	bday = Profile.objects.all()
	ss = str(today)
	for brith in bday:
		try:
			if brith.dob[5:] == ss[5:]:
				if brith.last_name == None or brith.last_name == '':
					print(brith.first_name)
					lenth.append(brith.dob)
					username_ids = brith.first_name
					ids_user.append(username_ids)
					username_s.append('Birthday')
				else:
					lenth.append(brith.dob)
					username_id = str(brith.first_name)+' '+str(brith.last_name)
					ids_user.append(username_id)
					username_s.append('Birthday')
		except:
			pass
	for data in update_obj:
		lenth.append(data.file_note_date)
		ids_user.append(data.userid)
		nameusera = Profile.objects.get(userid=data.userid)
		username_ids = nameusera.last_name
		if username_ids == None:
			username_ids = nameusera.first_name
			username_s.append(username_ids)
		else:
			username_id = str(nameusera.first_name)+' '+str(nameusera.last_name)
			username_s.append(username_id)
		today_follow.append(data.file_note_date)
	if len(lenth) == 0:
		notify = 0
	else:
		notify = len(lenth)
	loginuser = User.objects.get(username=request.user.username)
	ss = str(loginuser)
	split = ss.split('@' '')[0]
	try:
		img = User_Profile.objects.get(office_email=ss)
		if img.profile_pic == '':
			img = 'h' 
			imagedummy = 'h'
		else:
			img = User_Profile.objects.all().filter(office_email=ss)
			img = img
			imagedummy = 'h'
	except:
		img = User_Profile.objects.all().filter(office_email=ss)
		ss = len(img)
		if len(img) == 0:
			img = 'h'
			imagedummy = 'h'
	chahat = str(loginuser)
	all_datils = zip(ids_user,username_s)
	serchuser = Profile.objects.all()
	show_users_all = []
	for usersssss in serchuser:
		show_users_all.append(usersssss.first_name)
	chahat = str(loginuser)
	all_datils = zip(ids_user,username_s)
	print("x:-----------",x)
	if x != "":
		save = 'Information saved successfully'
	else:
		save = ''
		x = ''

	if 'chahat@edulaunchers.com' in users:
		print("dfsdfsdf")
		return render(request,'filenote_id1.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'file_note':file_note,'image':imagedummy,'show_users':show_users_all,'save':save})
	else:
		return render(request,'filenote_id.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'file_note':file_note,'image':imagedummy,'show_users':show_users_all,'save':save})
@login_required
def userinfo(request):
	all_us = Profile.objects.all().order_by('datetime').reverse()
	
	show_user = []
	for user_info in all_us:
		show_user.append(user_info.first_name)
	from datetime import date
	today = date.today()
	match = str(today)
	update_obj = FileNote.objects.filter(file_note_date=today)
	lenth = []
	ids_user = []
	today_follow = []
	username_s = []
	bday = Profile.objects.all()
	ss = str(today)
	for brith in bday:
		try:
			if brith.dob[5:] == ss[5:]:
				if brith.last_name == None or brith.last_name == '':
					print(brith.first_name)
					lenth.append(brith.dob)
					username_ids = brith.first_name
					ids_user.append(username_ids)
					username_s.append('Birthday')
				else:
					lenth.append(brith.dob)
					username_id = str(brith.first_name)+' '+str(brith.last_name)
					ids_user.append(username_id)
					username_s.append('Birthday')
		except:
			pass
	for data in update_obj:
		lenth.append(data.file_note_date)
		ids_user.append(data.userid)
		nameusera = Profile.objects.get(userid=data.userid)
		username_ids = nameusera.last_name
		if username_ids == None:
			username_ids = nameusera.first_name
			username_s.append(username_ids)
		else:
			username_id = str(nameusera.first_name)+' '+str(nameusera.last_name)
			username_s.append(username_id)
		today_follow.append(data.file_note_date)
	if len(lenth) == 0:
		notify = 0
	else:
		notify = len(lenth)
	loginuser = User.objects.get(username=request.user.username)
	ss = str(loginuser)
	split = ss.split('@' '')[0]
	try:
		img = User_Profile.objects.get(office_email=ss)
		if img.profile_pic == '':
			img = 'h' 
			imagedummy = 'h'
		else:
			img = User_Profile.objects.all().filter(office_email=ss)
			img = img
			imagedummy = 'h'
	except:
		img = User_Profile.objects.all().filter(office_email=ss)
		ss = len(img)
		if len(img) == 0:
			img = 'h'
			imagedummy = 'h'
	all_datils = zip(ids_user,username_s)
	loginuser = User.objects.get(username=request.user.username)
	chahat = str(loginuser)
	user = Profile.objects.all().order_by('datetime').reverse()
	user_ids = []
	fullname = []
	allid =[]
	users = Followup.objects.all()
	idsnew=[]
	datenew=[]
	references = []
	user_ids_login = []
	Emailsa = []
	contact_numbers = []
	firstnames = []
	all_users = []
	for detail in user:
		qs = detail.inquiry_status 
		if qs == 'Lead':
			all_user = Profile.objects.get(userid=detail.userid)
			all_users.append(all_user)
			ids = detail.userid
			allid.append(ids)
			datetime = detail.datetime
			date = datetime.strftime("%Y-%m-%d %H:%M")
			idsnew.append(ids)
			datenew.append(date)
			references.append(detail.reference)
			ddddd = detail.advisor
			try:
				user_admin = ddddd.split('@' '')[0]
			except:
				user_admin = detail.advisor
			user_ids_login.append(user_admin)
			first_ = detail.first_name
			last_ = detail.last_name
			if last_ ==  None:
				name = first_
			else:
				name = str(first_)+' '+str(last_)
			Emails = detail.Email
			contact_number = detail.contact_number
			fullname.append(name)
			Emailsa.append(Emails)
			contact_numbers.append(contact_number)
			firstnames.append(first_)
		
	if idsnew == '':
			le = 'No lead available.'
	else:
		le = ''
	lens1=len(user_ids)
	lens2=len(fullname)
	maxx=max([lens1,lens2])
	for i in range(1, maxx+1):
		if len(user_ids) <i:
			user_ids.append("")
		if len(fullname) <i:
			fullname.append("")
	Offices = 'Office'
	Facebooks = 'Facebook'
	loginusers = str(loginuser)
	userss = loginusers.split('@' '')[0]
	print(userss)
	alldetail = zip(idsnew,datenew,references,user_ids_login,fullname,Emailsa,contact_numbers)
	
	page = request.GET.get('page', 1)
	paginator = Paginator(all_users, 20)
	try:
		users = paginator.page(page)
	except PageNotAnInteger:
		users = paginator.page(1)
	except EmptyPage:
		users = paginator.page(paginator.num_pages)

	if 'chahat@edulaunchers.com' in chahat:
		return render(request, 'details1.html',{'le':le,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'alldetails':alldetail,'user_ids':allid,'loginuser':loginusers,'Offices':Offices,'Facebooks':Facebooks,'firstnames':firstnames,'image':imagedummy,'show_user':show_user,'users':users})
	else:
		return render(request, 'details.html',{'le':le,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'alldetails':alldetail,'user_ids':allid,'loginuser':loginusers,'Offices':Offices,'Facebooks':Facebooks,'firstnames':firstnames,'image':imagedummy,'show_user':show_user,'users':users})








@login_required
def todayfollow_up(request):
	today = date.today()
	match = str(today)
	today_follow = Followup.objects.filter(next_followup_notification=match)
	follow_up_id = []
	usernames = []
	date_follow_up = []
	for todays in today_follow:
		if match == todays.next_followup_notification:
			follow_up_id.append(todays.userid)
			details = Profile.objects.get(userid=todays.userid)
			usernam = details.first_name+' '+details.last_name
			usernames.append(usernam)
			date_follow_up.append(todays.next_followup_notification)
	follow_today = zip(follow_up_id,usernames,date_follow_up)
	return render(request,'today_follow_up.html',{'follow_up_user':follow_today})
@login_required
def updateprofile(request):
	serchuser = Profile.objects.all()
	print("serchuser:--",serchuser)
	show_users_all = []
	for users in serchuser:
		show_users_all.append(users.first_name)
	loginuser = User.objects.get(username=request.user.username)
	user_name = request.GET.get('info')
	print("updateprofile:--",updateprofile)
	details = Profile.objects.get(userid=user_name)
	inquiry_statuss = details.inquiry_status
	prefixs = details.prefix
	username = details.first_name
	middle_name = details.middle_name
	last_name = details.last_name
	dob = details.dob
	Email = details.Email
	contact_number = details.contact_number
	Address = details.Address
	correspondence_address = details.correspondence_address
	Nationality = details.Nationality
	Gender = details.Gender
	Marital_Status = details.Marital_Status
	Country_Preference_a = details.Country_Preference_a
	Country_Preference_b = details.Country_Preference_b
	Others_Country = details.Others_Country
	intake = details.intake
	if request.method =='POST':
		inquiry_stss = request.POST['statuss']
		search = request.POST['pre-name']
		update_obj = Profile.objects.get(userid=user_name)
		f_name = request.POST['first-name']
		m_name = request.POST['middle-name']
		l_name = request.POST['Last-name']
		dobs = request.POST['birthday']
		print("dobs",dobs)
		emails = request.POST['email']
		numbers = request.POST['number']
		Genderss = request.POST['Genders']
		Statusa = request.POST['Status']
		Nationalit = request.POST['Nationalitys']
		homeaddresssss = request.POST['homeaddresss']
		titles = request.POST['title']
		countryAs = request.POST['countryA']
		countrybs = request.POST['countryB']
		Othersss = request.POST['Otherss']
		Intakestarts = request.POST['Intakestart']
		update_obj.inquiry_status= inquiry_stss
		update_obj.prefix= search
		update_obj.first_name= f_name
		update_obj.middle_name= m_name
		update_obj.last_name= l_name
		update_obj.dob= dobs
		update_obj.Email= emails
		update_obj.contact_number=numbers
		update_obj.Address=homeaddresssss
		update_obj.correspondence_address=titles
		update_obj.Nationality=Nationalit
		update_obj.Gender=Genderss
		update_obj.Marital_Status=Statusa
		update_obj.Country_Preference_a=countryAs
		update_obj.Country_Preference_b=countrybs
		update_obj.Others_Country=Othersss
		update_obj.intake=Intakestarts
		update_obj.save()
		details = Profile.objects.get(userid=user_name)
		prefixs = details.prefix
		username = details.first_name
		middle_name = details.middle_name
		last_name = details.last_name
		dob = details.dob
		Email = details.Email
		contact_number = details.contact_number
		Address = details.Address
		correspondence_address = details.correspondence_address
		Nationality = details.Nationality
		Gender = details.Gender
		Marital_Status = details.Marital_Status
		Country_Preference_a = details.Country_Preference_a
		Country_Preference_b = details.Country_Preference_b
		Others_Country = details.Others_Country
		intake = details.intake
		return redirect('/update/?info='+str(user_name))
	today = date.today()
	match = str(today)
	update_obj = FileNote.objects.filter(file_note_date=today)
	lenth = []
	ids_user = []
	today_follow = []
	username_s = []
	bday = Profile.objects.all()
	ss = str(today)
	for brith in bday:
		try:
			if brith.dob[5:] == ss[5:]:
				if brith.last_name == None or brith.last_name == '':
					print(brith.first_name)
					lenth.append(brith.dob)
					username_ids = brith.first_name
					ids_user.append(username_ids)
					username_s.append('Birthday')
				else:
					lenth.append(brith.dob)
					username_id = str(brith.first_name)+' '+str(brith.last_name)
					ids_user.append(username_id)
					username_s.append('Birthday')
		except:
			pass
	for data in update_obj:
		# if match == data.next_followup_notification:
		lenth.append(data.file_note_date)
		ids_user.append(data.userid)
		nameusera = Profile.objects.get(userid=data.userid)
		username_ids = nameusera.last_name
		if username_ids == None:
			username_ids = nameusera.first_name
			username_s.append(username_ids)
		else:
			username_id = str(nameusera.first_name)+' '+str(nameusera.last_name)
			username_s.append(username_id)
		today_follow.append(data.file_note_date)
	if len(lenth) == 0:
		notify = 0
	else:
		notify = len(lenth)
	loginuser = User.objects.get(username=request.user.username)
	
	ss = str(loginuser)
	split = ss.split('@' '')[0]
	try:
		img = User_Profile.objects.get(office_email=ss)
		print("img:=-----",img.profile_pic)
		if img.profile_pic == '':
			img = 'h' 
			imagedummy = 'h'
		else:
			print("---")
			img = User_Profile.objects.all().filter(office_email=ss)
			img = img
			imagedummy = 'h'
	except:
		img = User_Profile.objects.all().filter(office_email=ss)
		ss = len(img)
		if len(img) == 0:
			img = 'h'
			imagedummy = 'h'
	chahat = str(loginuser)
	all_datils = zip(ids_user,username_s)
	if 'chahat@edulaunchers.com' in chahat:
		return render(request, 'logs_details.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'user_name':user_name,'userid':prefixs,'username':username,'middle_name':middle_name,'last_name':last_name,'dob':dob,
		'Email':Email,'contact_number':contact_number,'Nationality':Nationality,'Gender':Gender,'Marital_Status':Marital_Status,'Address':Address,'correspondence_address':correspondence_address
		,'Country_Preference_a':Country_Preference_a,'Country_Preference_b':Country_Preference_b,'Others_Country':Others_Country,'intake':intake,'image':imagedummy,'show_users':show_users_all,'inquiry_statuss':inquiry_statuss})
	else:
		return render(request, 'infoedit.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'user_name':user_name,'userid':prefixs,'username':username,'middle_name':middle_name,'last_name':last_name,'dob':dob,
		'Email':Email,'contact_number':contact_number,'Nationality':Nationality,'Gender':Gender,'Marital_Status':Marital_Status,'Address':Address,'correspondence_address':correspondence_address
		,'Country_Preference_a':Country_Preference_a,'Country_Preference_b':Country_Preference_b,'Others_Country':Others_Country,'intake':intake,'image':imagedummy,'show_users':show_users_all,'inquiry_statuss':inquiry_statuss})
@login_required
def followupuser_id(request):
	loginuser = User.objects.get(username=request.user.username)
	print("login user: - ---------------:------",loginuser)
	user_id =  request.GET.get('info')
	update_obj = Followup.objects.filter(userid=user_id)
	nameuser = Profile.objects.get(userid=user_id)
	lastfollowupmtexts = []
	lastfolowdates = []
	ids_ = []
	try:
		username_ida = nameuser.first_name+' '+nameuser.middle_name+' '+nameuser.last_name+' '+'('+nameuser.userid+')'
	except:
		pass
	try:
		username_ida = nameuser.first_name+' '+nameuser.middle_name+' '+'('+nameuser.userid+')'
	except:
		pass
	try:
		username_ida = nameuser.first_name+ '('+nameuser.userid+')'
	except:
		pass
	today = date.today()
	match = str(today)
	followuphandlernames = []
	for hello in update_obj:
		stype = hello.next_followup_notification
		print("stypestype",stype)
		followuphandlernames.append(hello.advisor)
		ids_.append(hello.userid)
		current_date = hello.lastfollowupdate
		now_scrapping = current_date.strftime("%Y-%m-%d %H:%M:%S")
		lastfolowdates.append(now_scrapping)
		lastfollowupmtexts.append(hello.last_follow_up_text)
		# if match == stype:
		# 	print("If conditions")
	if request.method == 'POST':
		followup_Comments = request.POST['Comments']
		next_follow_date = request.POST['Follow']
		print(followup_Comments,next_follow_date)
		obj = Followup.objects.create(
		userid =  Profile.objects.get(userid=user_id),
		advisor = loginuser,
		next_followup_notification = next_follow_date,
		last_follow_up_text = followup_Comments)
		return redirect('/followup/?info='+str(user_id))
	showdetails = zip(followuphandlernames,lastfolowdates,lastfollowupmtexts)
	users = str(loginuser)
	today = date.today()
	print(today)
	match = str(today)
	update_obj = Followup.objects.all()
	lenth = []
	ids_user = []
	today_follow = []
	username_swaq = []
	for data in update_obj:
		if match == data.next_followup_notification:
			lenth.append(data.next_followup_notification)
			ids_user.append(data.userid)
			nameusera = Profile.objects.get(userid=data.userid)
			username_ids = nameusera.last_name
			if username_ids == None:
				username_ids = nameusera.first_name
				username_s.append(username_ids)
			else:
				username_id = str(nameusera.first_name)+' '+str(nameusera.last_name)
				username_s.append(username_id)
			today_follow.append(data.next_followup_notification)
	if len(lenth) == 0:
		notify = 0
	else:
		notify = len(lenth)
	loginuser = User.objects.get(username=request.user.username)
	print("loginuser",loginuser)
	print("notify:",notify)
	ss = str(loginuser)
	split = ss.split('@' '')[0]
	try:
		img = User_Profile.objects.get(office_email=ss)
		print("img:=-----",img.profile_pic)
		if img.profile_pic == '':
			img = 'h' 
			imagedummy = 'h'
		else:
			print("---")
			img = User_Profile.objects.all().filter(office_email=ss)
			img = img
			imagedummy = 'h'
	except:
		img = User_Profile.objects.all().filter(office_email=ss)
		ss = len(img)
		if len(img) == 0:
			img = 'h'
			imagedummy = 'h'
	all_data = []
	db_user = Profile.objects.all()
	for user_names in db_user:
		all_data.append(user_names.first_name)

	chahat = str(loginuser)
	all_datils = zip(ids_user,username_swaq,today_follow)
	if 'chahat@edulaunchers.com' in users:
		return render(request,'singleuserfollowup1.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'username_id':username_ida, 'showdetails':showdetails,'user_id':user_id})
	else:
		return render(request,'singleuserfollowup.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'username_id':username_ida, 'showdetails':showdetails,'user_id':user_id,'image':imagedummy,'show_users':all_data})	
@login_required
def today_followupuser(request):
	loginuser = User.objects.get(username=request.user.username)
	user_id =  request.GET.get('fetch')
	update_obj = Followup.objects.filter(userid=user_id)
	nameuser = Profile.objects.get(userid=user_id)
	lastfollowupmtexts = []
	lastfolowdates = []
	ids_ = []
	try:
		username_id_id = nameuser.first_name+' '+nameuser.middle_name+' '+nameuser.last_name+' '+'('+nameuser.userid+')'
	except:
		pass
	try:
		username_id_id = nameuser.first_name+' '+nameuser.middle_name+' '+'('+nameuser.userid+')'
	except:
		pass
	try:
		username_id_id = nameuser.first_name+ '('+nameuser.userid+')'
	except:
		pass
	today = date.today()
	match = str(today)
	followuphandlernames = []
	for hello in update_obj:
		stype = hello.next_followup_notification
		followuphandlernames.append(hello.advisor)
		ids_.append(hello.userid)
		current_date = hello.lastfollowupdate
		now_scrapping = current_date.strftime("%Y-%m-%d %H:%M:%S")
		lastfolowdates.append(now_scrapping)
		lastfollowupmtexts.append(hello.last_follow_up_text)
	if request.method == 'POST':
		update_objs = Followup.objects.get(next_followup_notification=match)
		stypess = update_objs.next_followup_notification
		mys = stypess
		parts = mys.split('-')
		mysdd = parts[2] + '-' + parts[1] + '-' + parts[0]
		update_objs.next_followup_notification = mysdd
		update_objs.save()
		followup_Comments = request.POST['Comments']
		next_follow_date = request.POST['Follow']
		obj = Followup.objects.create(
		userid =  Profile.objects.get(userid=user_id),
		advisor = loginuser,
		next_followup_notification = next_follow_date,
		last_follow_up_text = followup_Comments)
		return redirect('/mainpage/')
	showdetails = zip(followuphandlernames,lastfolowdates,lastfollowupmtexts)
	today = date.today()
	print(today)
	match = str(today)
	update_obj = Followup.objects.all()
	lenth = []
	ids_user = []
	today_follow = []
	username_sww = []
	for data in update_obj:
		if match == data.next_followup_notification:
			lenth.append(data.next_followup_notification)
			ids_user.append(data.userid)
			nameusera = Profile.objects.get(userid=data.userid)
			username_ids = nameusera.last_name
			if username_ids == None:
				username_ids = nameusera.first_name
				username_s.append(username_ids)
			else:
				username_id = str(nameusera.first_name)+' '+str(nameusera.last_name)
				username_s.append(username_id)
			today_follow.append(data.next_followup_notification)
	if len(lenth) == 0:
		notify = 0
	else:
		notify = len(lenth)
	loginuser = User.objects.get(username=request.user.username)
	print("loginuser",loginuser)
	print("notify:",notify)
	ss = str(loginuser)
	split = ss.split('@' '')[0]
	try:
		img = User_Profile.objects.get(office_email=ss)
		print("img:=-----",img.profile_pic)
		if img.profile_pic == '':
			img = 'h' 
		else:
			print("---")
			img = User_Profile.objects.all().filter(office_email=ss)
			img = img
	except:
		img = User_Profile.objects.all().filter(office_email=ss)
		ss = len(img)
		if len(img) == 0:
			img = 'h'
	chahat = str(loginuser)
	all_datils = zip(ids_user,username_sww,today_follow)
	return render(request,'singleuserfollowup.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'username_id':username_id_id, 'showdetails':showdetails})
@login_required
def filenote(request):
	loginuser = User.objects.get(username=request.user.username)
	user_id =  request.GET.get('info')
	print("user_id",user_id)
	
	update_ob = FileNote.objects.filter(userid=user_id).order_by('date').reverse()
	# update_ob = reversed(update_ob)
	print(update_ob)
	nameuser = Profile.objects.get(userid=user_id)
	print("user_id:------------------",nameuser.first_name)
	if nameuser.first_name != None and nameuser.middle_name != None and nameuser.last_name != None :
		username_ids_4 = nameuser.first_name+' '+nameuser.last_name+' '+'('+nameuser.userid+')'
		print(username_ids_4)
	if nameuser.last_name == None:
		username_ids_4 = nameuser.first_name+' '+'('+nameuser.userid+')'
		print(username_ids_4)
	if nameuser.first_name != None and nameuser.last_name != None :
		username_ids_4 = nameuser.first_name+' '+nameuser.last_name+' '+'('+nameuser.userid+')'
		print(username_ids_4)
	# try:
	# 	username_ids_4 = nameuser.first_name+' '+nameuser.middle_name+' '+nameuser.last_name+' '+'('+nameuser.userid+')'
	# except:
	# 	pass
	# try:
	# 	username_ids_4 = nameuser.first_name+' '+nameuser.middle_name+' '+'('+nameuser.userid+')'
	# except:
	# 	pass
	# try:
	# 	username_ids_4 = nameuser.first_name+  '('+nameuser.userid+')'
	# except:
	# 	pass
	dates = []
	filenot = []
	handlers = []
	
	for filenotes in update_ob:
		current_dates = filenotes.add_file_datetime
		dates.append(current_dates)
		filenot.append(filenotes.note)
		handlers.append(filenotes.advisor)
	import datetime
	now = datetime.datetime.now()
	today_date = now.strftime("%d-%m-%Y %H:%M:%S")
	if request.method =='POST':
		file = request.POST['Comments']
		try:
			date_note = request.POST['Follow']
		except:
			date_note = ''
			pass
		print('date_note',date_note)
		obj = FileNote.objects.create(
			userid =  Profile.objects.get(userid=user_id),
			note = file,
			advisor = loginuser,
			file_note_date = date_note,
			add_file_datetime=today_date)
		return redirect('/filenote/?info='+str(user_id))
	
	showdetails = zip(filenot,handlers,dates)	
	today = date.today()
	match = str(today)
	update_obj = FileNote.objects.filter(file_note_date=today)
	lenth = []
	ids_user = []
	today_follow = []
	username_sss = []
	bday = Profile.objects.all()
	ss = str(today)
	for brith in bday:
		try:
			if brith.dob[5:] == ss[5:]:
				if brith.last_name == None or brith.last_name == '':
					print(brith.first_name)
					lenth.append(brith.dob)
					username_ids = brith.first_name
					ids_user.append(username_ids)
					username_sss.append('Birthday')
				else:
					lenth.append(brith.dob)
					username_id = str(brith.first_name)+' '+str(brith.last_name)
					ids_user.append(username_id)
					username_sss.append('Birthday')
		except:
			pass
	for data in update_obj:
		# if match == data.next_followup_notification:
		lenth.append(data.file_note_date)
		ids_user.append(data.userid)
		nameusera = Profile.objects.get(userid=data.userid)
		username_ids = nameusera.last_name
		if username_ids == None:
			username_ids = nameusera.first_name
			username_sss.append(username_ids)
		else:
			username_id = str(nameusera.first_name)+' '+str(nameusera.last_name)
			username_sss.append(username_id)
		today_follow.append(data.file_note_date)
	if len(lenth) == 0:
		notify = 0
	else:
		notify = len(lenth)
	ss = str(loginuser)
	split = ss.split('@' '')[0]
	try:
		img = User_Profile.objects.get(office_email=ss)
		if img.profile_pic == '':
			img = 'h' 
			imagedummy = 'h'
		else:
			img = User_Profile.objects.all().filter(office_email=ss)
			img = img
			imagedummy = 'h'
	except:
		img = User_Profile.objects.all().filter(office_email=ss)
		ss = len(img)
		if len(img) == 0:
			img = 'h'
			imagedummy = 'h'
	all_data = []
	db_user = Profile.objects.all()
	for user_names in db_user:
		all_data.append(user_names.first_name)
	all_datils = zip(ids_user,username_sss)
	chahat = str(loginuser)
	if 'chahat@edulaunchers.com' in chahat:
		return render(request,'file_note1.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'showdetails':showdetails,'username_ids':username_ids_4,'user_id':user_id,'image':imagedummy,'show_users':all_data})
	else:
		return render(request,'file_note.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'showdetails':showdetails,'username_ids':username_ids_4,'user_id':user_id,'image':imagedummy,'show_users':all_data})
@login_required
def edit_file_notes(request):
	today = date.today()
	match = str(today)
	update_obj = FileNote.objects.filter(file_note_date=today)
	lenth = []
	ids_user = []
	today_follow = []
	username_s = []
	bday = Profile.objects.all()
	ss = str(today)
	for brith in bday:
		try:
			if brith.dob[5:] == ss[5:]:
				if brith.last_name == None or brith.last_name == '':
					print(brith.first_name)
					lenth.append(brith.dob)
					username_ids = brith.first_name
					ids_user.append(username_ids)
					username_s.append('Birthday')
				else:
					lenth.append(brith.dob)
					username_id = str(brith.first_name)+' '+str(brith.last_name)
					ids_user.append(username_id)
					username_s.append('Birthday')
		except:
			pass
	for data in update_obj:
		lenth.append(data.file_note_date)
		ids_user.append(data.userid)
		nameusera = Profile.objects.get(userid=data.userid)
		# try:
		username_ids = nameusera.last_name
		if username_ids == None:
			username_ids = nameusera.first_name
			username_s.append(username_ids)
		else:
			username_id = str(nameusera.first_name)+' '+str(nameusera.last_name)
			username_s.append(username_id)
		# except:
		# 	pass
		today_follow.append(data.file_note_date)
	if len(lenth) == 0:
		notify = 0
	else:
		notify = len(lenth)
	loginuser = User.objects.get(username=request.user.username)
	ss = str(loginuser)
	split = ss.split('@' '')[0]
	try:
		img = User_Profile.objects.get(office_email=ss)
		if img.profile_pic == '':
			img = 'h' 
			imagedummy = 'h'
		else:
			print("---")
			img = User_Profile.objects.all().filter(office_email=ss)
			img = img
			imagedummy = 'h'
	except:
		img = User_Profile.objects.all().filter(office_email=ss)
		ss = len(img)
		if len(img) == 0:
			img = 'h'
			imagedummy = 'h'
	
	all_datils = zip(ids_user,username_s)
	
	serchuser = Profile.objects.all()
	show_users_all = []
	for users in serchuser:
		show_users_all.append(users.first_name)
	loginuser = User.objects.get(username=request.user.username)
	edit = request.GET.get('editinfo')
	user_id = edit.split(' ' '')[0]
	ss = edit.split(' ' '')[1]+' '+edit.split(' ' '')[2]
	dates =  FileNote.objects.get(add_file_datetime=ss)
	show_old_text = dates.note
	
	gfg = BeautifulSoup(show_old_text)
	res = gfg.get_text()
	# print(res)
	
	if 'admin' in str(loginuser) or 'chahat@edulaunchers.com' in str(loginuser):
		if request.method == 'POST':
			print("dates:--------",dates)
			file = request.POST['Comments']
			dates.note = file
			dates.save()
			return redirect('/filenote/?info='+str(user_id))	
		return render(request,'edit_file_notes.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'image':imagedummy,'show_users':show_users_all,'show_old_texts':res})
	else:
		print("esle:------------------------")
		return redirect('/filenote/?info='+str(user_id))
@login_required
def followsubmit(request):
	user_id =  request.GET.get('fetch')
	print("user_id",user_id)
	today = date.today()
	match = str(today)
	update_obj = FileNote.objects.filter(file_note_date=today)
	lenth = []
	ids_user = []
	today_follow = []
	username_s = []
	bday = Profile.objects.all()
	ss = str(today)
	for brith in bday:
		try:
			if brith.dob[5:] == ss[5:]:
				if brith.last_name == None or brith.last_name == '':
					print(brith.first_name)
					lenth.append(brith.dob)
					username_ids = brith.first_name
					ids_user.append(username_ids)
					username_s.append('Birthday')
				else:
					lenth.append(brith.dob)
					username_id = str(brith.first_name)+' '+str(brith.last_name)
					ids_user.append(username_id)
					username_s.append('Birthday')
		except:
			pass
	for data in update_obj:
		# if match == data.next_followup_notification:
		lenth.append(data.file_note_date)
		ids_user.append(data.userid)
		nameusera = Profile.objects.get(userid=data.userid)
		username_ids = nameusera.last_name
		if username_ids == None:
			username_ids = nameusera.first_name
			username_s.append(username_ids)
		else:
			username_id = str(nameusera.first_name)+' '+str(nameusera.last_name)
			username_s.append(username_id)
		today_follow.append(data.file_note_date)
	if len(lenth) == 0:
		notify = 0
	else:
		notify = len(lenth)
	loginuser = User.objects.get(username=request.user.username)
	print("loginuser",loginuser)
	print("notify:",notify)
	ss = str(loginuser)
	split = ss.split('@' '')[0]
	try:
		img = User_Profile.objects.get(office_email=ss)
		print("img:=-----",img.profile_pic)
		if img.profile_pic == '':
			img = 'h' 
			imagedummy = 'h'
		else:
			print("---")
			img = User_Profile.objects.all().filter(office_email=ss)
			img = img
			imagedummy = 'h'
	except:
		img = User_Profile.objects.all().filter(office_email=ss)
		ss = len(img)
		if len(img) == 0:
			img = 'h'
			imagedummy = 'h'
	chahat = str(loginuser)
	all_datils = zip(ids_user,username_s)
	serchuser = Profile.objects.all()
	show_users_all = []
	for users in serchuser:
		show_users_all.append(users.first_name)
	update_objs = FileNote.objects.filter(userid=user_id)
	update_objs = reversed(update_objs)
	nameuser = Profile.objects.get(userid=user_id)
	lastfollowupmtexts = []
	lastfolowdates = []
	ids_ = []
	try:
		username_id_id = nameuser.first_name+' '+nameuser.middle_name+' '+nameuser.last_name+' '+'('+nameuser.userid+')'
	except:
		pass
	try:
		username_id_id = nameuser.first_name+' '+nameuser.middle_name+' '+'('+nameuser.userid+')'
	except:
		pass
	try:
		username_id_id = nameuser.first_name + '('+nameuser.userid+')'
	except:
		pass
	import datetime
	now = datetime.datetime.now()
	today_date = now.strftime("%Y-%m-%d %H:%M:%S")
	# try:
	followuphandlernames = []
	for hello in update_objs:
		stype = hello.file_note_date
		followuphandlernames.append(hello.advisor)
		ids_.append(hello.userid)
		current_date = hello.date
		now_scrapping = current_date.strftime("%Y-%m-%d %H:%M:%S")
		lastfolowdates.append(now_scrapping)
		lastfollowupmtexts.append(hello.note)
	if request.method == 'POST':
		update_objss = FileNote.objects.get(file_note_date=match,userid=user_id)
		print('update_objss',update_objss)
		stypess = update_objss.file_note_date
		mys = stypess
		parts = mys.split('-')
		mysdd = parts[2] + '-' + parts[1] + '-' + parts[0]
		update_objss.file_note_date = mysdd
		update_objss.save()
		followup_Comments = request.POST['Comments']
		next_follow_date = request.POST['Follow']
		if next_follow_date == '':
			next_follow_date = ''
		else:
			next_follow_date = next_follow_date
		obj = FileNote.objects.create(
		userid =  Profile.objects.get(userid=user_id),
		advisor = loginuser,
		file_note_date = next_follow_date,
		add_file_datetime=today_date,
		note = followup_Comments)
		return redirect('/FollowUp/?fetch='+str(user_id))
	# except:
	# 	pass
	showdetails = zip(followuphandlernames,lastfolowdates,lastfollowupmtexts)
	chahat = str(loginuser)
	if 'chahat@edulaunchers.com' in chahat:
		return render(request,'testlogs.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'image':imagedummy,'show_users':show_users_all,'username_id':username_id_id, 'showdetails':showdetails,'user_id':user_id})
	else:
		return render(request,'submitfollowup.html',{'loginuser':loginuser,'hotel_images' : img,'notify':notify,'all_datils':all_datils,'image':imagedummy,'show_users':show_users_all,'username_id':username_id_id, 'showdetails':showdetails,'user_id':user_id})
