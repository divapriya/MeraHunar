from django.conf.urls import url
from django.contrib import auth
from counselling import views


urlpatterns = [
	url(r'^$',views.HomePage,name="homepage"),
	url(r'^organizationsearchlocation/(?P<location>.*)$',views.OrganizationSearchBy_Location, name='organizationbylocation'),
	url(r'^organizationsearchfield/(?P<field>.*)$',views.OrganizationSearchBy_Field, name='organizatiosearchbyfield'),
	url(r'^organizationsearchexp/(?P<field1>.*)/(?P<field2>.*)$',views.OrganizationSearchBy_Year, name='organizationsearchbyexp'),
	url(r"^singleorganization/(?P<pk>.*)$",views.get_single_organization,name="singleorganization"),
	url(r"^cregister",views.counsellors_register,name="councilregister"),
	url(r"^organization",views.get_all_organization,name="allorganizations"),
	url(r"^add_comment/(?P<pk>.*)$",views.add_comment_organization,name="add_comment"),
	url(r'^freelancersearchjobrole/(?P<jobrole>.*)$',views.FreelancerSearchBy_JobRoles, name='freelancerbyjob'),
	url(r'^freelancersearchfield/(?P<field>.*)$',views.FreelancerSearchBy_Field, name='freelancerbyfield'),
	url(r'^freelancersearchexp/(?P<field1>.*)/(?P<field2>.*)$',views.FreelancerSearchBy_Exp, name='freelancersearchbyexp'),
	url(r"^singlefreelancer/(?P<pk>.*)$",views.get_single_freelancer,name="singlefreelancer"),
	url(r"^fregister",views.freelancers_register,name="freelancerregister"),
	url(r"^freelancerblog/(?P<pk>.*)$",views.get_freelancer_blog,name="singlefreelancerblog"),
	url(r"^freelancer",views.get_all_freelancer,name="allfreelancer"),

	url(r'^onlinecounselling/$', views.online_counselling, name='onlinecounselling'),]
#	url(r'^logout/$', views.LogoutRequest, name='login'),
#	url(r'^profile/$', views.Profile, name='profile'),
#    url(r'^$', views.DrinkerRegistration, name='registration'),]

