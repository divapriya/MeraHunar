from django.db import models
from jobportal.models.commonModels import *
#from users.models import Users,Organizers,Freelancers
#from multiselectfield import MultiSelectField
from mongoengine import *

class User_Details(Document):
	name=StringField(max_length=200, default='anonymous user')
	details=ReferenceField(User)   ##Added
	qualification=ListField(StringField(), required=False)
	extra_curricullums=ListField(StringField(), required=False)
	employment=ListField(StringField(), required=False)
	personalinterest=ListField(StringField(), required=False)
	qualification_preference=IntField(required=False,default=1)
	extra_curricullums_preference =IntField(required=False,default=1)
	employment_preference=IntField(required=False,default=1)
	personalinterest_preference =IntField(required=False,default=1)
	#slug=models.SlugField(unique=True,null=True)
	def __str__(self):
		return self.name

class Organization_Details(Document):
	name=StringField(max_length=200, default='anonymous user')
	#slug=models.SlugField(unique=True,null=True)
	details=ReferenceField(User)	##Added
	#ranking=ReferenceField(Ranking_Organization)
	#comments=ReferenceField(Comment_Organization)	
	def __str__(self):
		return self.name

class Individual_Details(Document):
	name=StringField(max_length=200, default='anonymous user')
	#slug=models.SlugField(unique=True,null=True)
	details=ReferenceField(User)	##Added
	#ranking=ReferenceField(Ranking_Individual)
	#comments=ReferenceField(Comment_Individual)
	
	def __str__(self):
		return self.name


class Comment_Organization(Document):
	by=ReferenceField(User)    ##Added
	date=LongField()
	comment=StringField(required=True)
	rating=IntField()
	attribute=ReferenceField(Organization_Details)

	def __str__(self):
		return self.comment

class Comment_Individual(Document):
	by=ReferenceField(User) ##Added
	date=LongField()
	comment=StringField(required=True)
	ranking=IntField()
	attribute=ReferenceField(Individual_Details)

	def __str__(self):
		return self.comment

class Ranking_Organization(Document):
	by=ReferenceField(User)   ##Added
	date=LongField()
	ranking=FloatField(required=True)
	attribute=ReferenceField(Organization_Details)

	def __float__(self):
		return self.ranking

class Ranking_Individual(Document):
	by=ReferenceField(User)   ##Added
	date=LongField()
	ranking=FloatField(required=True)
	attribute=ReferenceField(Individual_Details)

	def __float__(self):
		return self.ranking

class Blog(Document):
	of=ReferenceField(Individual_Details)
	#qestions=ListField(ReferenceField(Question))
	##answers=ReferenceField(Answer)
	
class Question(Document):
	by=ReferenceField(User)
	date=LongField()
	qes=StringField()
	
	attribute=ReferenceField(Blog)

class Answer(Document):
	by=ReferenceField(Individual_Details)
	date=LongField()
	ans=StringField()
	attribute=ReferenceField(Question)










# Create your models here.
