from django.conf.urls import  url
from vehicle import views
urlpatterns = [
		url(r'^$',views.user_login,name='user_login'),
		url(r'^index2/requisition/(?P<car_name>[\w|\W]+)/$',views.requisition_form,name='requisition_form'),
		url(r'^index2/$',views.index2,name='index2'),
		url(r'^logout/$',views.user_logout,name='user_logout'),
		url(r'^inbox/$',views.user_inbox,name='user_inbox'),
		url(r'^inbox/(?P<app_no>[\w|\W]+)/$',views.print_status,name='print_status'),
		url(r'^jd_inbox/$',views.jd_inbox,name='jd_inbox'),
		url(r'^index2/fb_list/(?P<fb_no>[\w|\W]+)/$',views.fb_userdetail_cum_reply,name='fb_userdetail_cum_reply'),
		url(r'^index2/fb_list/$',views.fb_user_list,name='fb_user_list'),
		url(r'^index2/feedback/$',views.submit_fb,name='feedback'),
		url(r'^index2/feedback_list/$',views.fb_list,name='fb_list'),
		url(r'^index2/enter_date/$',views.enter_date,name='enter_date'),
		url(r'^index2/(?P<date1>[-\w]+)/$',views.daily_report,name='daily_report'),
		url(r'^jd_inbox/(?P<fb_no>[\w|\W]+)/reply/$',views.fb_reply,name='fb_reply'),
		url(r'^jd_inbox/(?P<fb_no>[\w|\W]+)/$',views.fb_detail,name='fb_detail'),
		]	