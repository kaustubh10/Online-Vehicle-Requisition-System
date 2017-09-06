from django.contrib import admin
from vehicle.models import UserProfile,UserInbox,Vehicle,Slot,FeedBack,FeedbackReply

class UserInboxAdmin(admin.ModelAdmin):

	readonly_fields = ('app_sub_time',)
	 
admin.site.register(UserProfile)
admin.site.register(UserInbox,UserInboxAdmin)
admin.site.register(Vehicle)
admin.site.register(Slot)
admin.site.register(FeedBack)
admin.site.register(FeedbackReply)
# Register your models here.
