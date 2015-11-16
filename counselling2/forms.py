
from django import forms
from django.forms import ModelForm,widgets
from counselling.models import User_Details,Comment_Individual,Comment_Organization,Ranking_Organization,Ranking_Individual
from jobportal.models.commonModels import *
#from users.models import Drinker,Users,Organizers,Freelancers

QUALIFICATION_CHOICES=(('CA','CA'),('B.Tech','B.Tech')) #to be changed ,input to be taken from text file
EXTRACURRICS_CHOICES=(('sports','sports'),('arts','sports'))
POSTS_CHOICES=(('engineer','engineer'),('consultant','consultant'))
INTEREST_CHOICES=(('cooking','cooking'),('dancing','dancing'))
PREFER_CHOICES=('qualification','extra_curricullums','pastemployment','personalinterest')

class UserPreference(ModelForm):
	qualification=forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple, choices=QUALIFICATION_CHOICES)
	extra_curricullums=forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple, choices=EXTRACURRICS_CHOICES)
	employment=forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple, choices=POSTS_CHOICES)
	personalinterest=forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple, choices=INTEREST_CHOICES)
	qualification_preference = forms.IntegerField(min_value=1, max_value=5)
	extra_curricullums_preference = forms.IntegerField(min_value=1, max_value=5)
	employment_preference = forms.IntegerField(min_value=1, max_value=5)
	personalinterest_preference = forms.IntegerField(min_value=1, max_value=5)
	#preference=forms.ChoiceField(required=True, choices = PREFER_CHOICES, widget = forms.Select)
	
	class Meta:
		model=User_Details
		fields=('qualification','extra_curricullums','employment','personalinterest','qualification_preference','extra_curricullums_preference','employment_preference','personalinterest_preference')



class CommentFormOrganization(ModelForm):
    comment = forms.CharField(widget=forms.Textarea)

    class Meta:
		model=Comment_Organization
		exclude=('comment',)

