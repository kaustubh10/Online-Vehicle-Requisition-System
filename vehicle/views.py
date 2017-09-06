from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import  render,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from vehicle.models import UserProfile,UserInbox,Vehicle,Slot,FeedBack,FeedbackReply
from vehicle.forms import UserInboxForm,UserProfileForm,FeedBackForm,FeedbackReplyForm
from datetime import date
# Create your views here.


def index2(request):

	if request.user.is_authenticated():
		li = []
		c = Vehicle.objects.all()
		for i in c:
			sl = Slot.objects.filter(veh=i)
			li.append(sl)
		liste = zip(c,li)
		user = get_object_or_404(UserProfile,user=request.user)

	return render(request,'index2.html',{'c':c,'li':li,'user':user,'sl':sl,'liste':liste})

def user_login(request):

	if request.method=='POST':

		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username,password=password)

		if user:

			if user.is_active:

				login(request,user)
				return HttpResponseRedirect('/vehicle/index2/')
			else:
				return HttpResponse('Your account is inactive')
		else:
			return HttpResponse("Invalid username/password")

	else:
		return render(request,'login.html',{})

def user_logout(request):
	logout(request)

	return HttpResponseRedirect('/vehicle/')

def requisition_form(request,car_name):

	if request.user.is_authenticated():
		a = get_object_or_404(UserProfile,user=request.user)
		b = get_object_or_404(Vehicle,veh_name=car_name)
		if request.method == "POST":
			instance = UserInbox(user=a,veh=b)
			form = UserInboxForm(request.POST,instance=instance)
			form2 = UserProfileForm(request.POST or None,instance=a)
			
			if form.is_valid() and form2.is_valid():
				
				inbox = form.save(commit=False)
				contact = form2.save(commit=False)
				contact.save()
				inbox.status = 'Pending'
				a.seqno += 1
				inbox.app_no = '00' + a.user.username + str(a.seqno) 
				inbox.save()
				a.save()
				return update_status(request,inbox.app_no,car_name)
			else:
				print form.errors
		else:
			form = UserInboxForm()
			data = {
			'contact': a.contact
			}
			form2 = UserProfileForm(initial=data)

			return render(request,'requistion_form.html',{'form':form,'form2':form2,'a':a,'b':b})
def user_inbox(request):

	if request.user.is_authenticated():
		a = get_object_or_404(UserProfile,user=request.user)
		c = UserInbox.objects.filter(user=a).order_by('-app_sub_time')
		context = {
			'a':a,
			'c':c,
		}
	else:
		context = {}

	return render(request,'user_inbox.html',context)

def jd_inbox(request):

	if request.user.is_authenticated():

		c = UserInbox.objects.order_by('-app_sub_time')
		context = {
			'c':c,
		}
	else:
		context = {}

	return render(request,'jd_inbox.html',context)	

def update_status(request,app_no,car_name):

	if request.user.is_authenticated():
		ui = get_object_or_404(UserInbox,app_no=app_no)
		tmp = get_object_or_404(Vehicle,veh_name=car_name)
		sl = Slot.objects.filter(veh=tmp)
		flag = 1
		for s in sl:
			if ui.from_time>=s.from_t and ui.from_time<=s.to_t:
				flag = 0
		if flag==0:
			ui.status = 'Rejected'
		else:
			ui.status = 'Sanctioned'
			o = Slot(from_t=ui.from_time,to_t=ui.to_time,veh=tmp)
			o.save()
		ui.save()
		return HttpResponseRedirect('/vehicle/index2/')

	
def submit_fb(request):

	if request.user.is_authenticated():
		a = get_object_or_404(UserProfile,user=request.user)
		if request.method=="POST":
			instance = FeedBack(user=a)
			form = FeedBackForm(request.POST or None,instance=instance)
			if form.is_valid():
				fb = form.save(commit=False)
				a.seqno += 1
				tmp = '01' + request.user.username + str(a.seqno)
				fb.fb_no = tmp
				fb.save()
				a.save()
				return HttpResponseRedirect('/vehicle/index2/')
			else:
				print form.errors
		else:
			form = FeedBackForm()

			return render(request,'feedback_form.html',{'form':form,'a':a})

def fb_list(request):

	if request.user.is_authenticated():
		c = FeedBack.objects.all().order_by('-fb_sub_time')

		return render(request,'fb_list.html',{'c':c})

def fb_detail(request,fb_no):

	if request.user.is_authenticated():

		i = get_object_or_404(FeedBack,fb_no=fb_no)

		return render(request,'feedback_detail.html',{'i':i})

def fb_reply(request,fb_no):

	if request.user.is_authenticated():
		a = get_object_or_404(FeedBack,fb_no=fb_no)
		instance = FeedbackReply(feedback=a)
		if request.method=="POST":

			form = FeedbackReplyForm(request.POST or none,instance=instance)
			if form.is_valid():
				c = form.save(commit=False)
				a.status = 1
				c.save()
				a.save()
				return HttpResponseRedirect('/vehicle/jd_inbox/')
			else:
				print form.errors
		else:
			form = FeedbackReplyForm()
			return render(request,'reply.html',{'form':form})

def fb_user_list(request):
	
	if request.user.is_authenticated():	
		a = get_object_or_404(UserProfile,user=request.user)
		c = FeedBack.objects.filter(user=a)
		return render(request,'fb_user_list.html',{'c':c})

def fb_userdetail_cum_reply(request,fb_no):

	if request.user.is_authenticated():
		a = get_object_or_404(FeedBack,fb_no=fb_no)
		b = get_object_or_404(FeedbackReply,feedback=a)
		return render(request,'last_page.html',{'a':a,'b':b})

def print_status(request,app_no):

	i = get_object_or_404(UserInbox,app_no=app_no)
		
	return render(request,'print_status.html',{'i':i})

def daily_report(request,date1):

	s1 = int(date1[0] + date1[1] + date1[2] + date1[3])
	s2 = int(date1[5] + date1[6]) 
	s3 = int(date1[8] + date1[9])
	date2 = date(s1,s2,s3)
	i = UserInbox.objects.filter(app_sub_time__date=date2)
	"""i = UserInbox.objects.filter(app_sub_time__date=date2)"""
	return render(request,'daily_report.html',{'i':i})

def enter_date(request):

	if request.method=='POST':

		date1 = request.POST.get('date')
		
		st = '/vehicle/index2/' + date1 + '/'
		return HttpResponseRedirect(st)
	else:
		return render(request,'enter_date.html',{})	


	