from django import forms
from vehicle.models import UserInbox,FeedBack,UserProfile,FeedbackReply
from django.contrib.admin.widgets import AdminDateWidget
class UserProfileForm(forms.ModelForm):

	class Meta:
		model = UserProfile
		fields = ('contact',)
		
class UserInboxForm(forms.ModelForm):

	date_of_journey = forms.DateField(widget=AdminDateWidget)
	from_time = forms.TimeField(help_text='Start time')
	to_time = forms.TimeField(help_text='End time')
	purpose = forms.CharField(max_length=128,help_text='Your purpose of journey')
	source = forms.CharField(max_length=128,help_text='Where required ?')
	destination = forms.CharField(max_length=128,help_text='Where you want to go?')
	others = forms.CharField(max_length=128,help_text='Other persons: ')
	class Meta:
		model = UserInbox
		fields = ('date_of_journey','from_time','to_time','purpose','source','destination','others')


class FeedBackForm(forms.ModelForm):

	Suggestions = forms.CharField(max_length=128,widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Please give suggestions for amendments','rows':'5'}))
	Remarks = forms.CharField(max_length=128,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'remarks','required':True}))
	class Meta:
		model = FeedBack
		fields = ('Suggestions','Remarks')

class FeedbackReplyForm(forms.ModelForm):

	reply = forms.CharField(max_length=128,widget=forms.Textarea())
	class Meta:
		model = FeedbackReply
		fields = ('reply',)

