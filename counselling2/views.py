from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from counselling.models import *
from counselling.serializers import User_Details_Serializer
from jobportal.constants import CustomStatus, AttachmentTypesPaths
from jobportal.utilities import *
#from counselling.forms import UserPreference,CommentFormOrganization
#from users.models import Drinker,Users,Organizers,Freelancers
from jobportal.models.commonModels import *
from django.template.defaultfilters import slugify
import mongoengine

def HomePage(request):
    return render(request,'counselling/home.html',{})


@api_view(['GET','POST'])
def online_counselling(request):
    if request.method == 'GET':
        return render(request, 'counselling/user_preference.html',{})

    
    if request.method == 'POST':
        if(True):
        #if UserDetail.is_valid():
            #email = request.data.get('email').lower()#########################Ask
            email = request.session.get('email')############################################################################Ask
            details=User.objects(email=email).first()
            name=User.objects(email=email).first().firstName  ##Added
            #slug=slugify(request.user)

            qualification = request.data.get('qualification')
            extra_curricullums = request.data.get('extra_curricullums ')
            employment= request.data.get('employment')
            personalinterest = request.data.get('personalinterest')
            qualification_preference=request.data.get('qualification_preference')
            extra_curricullums_preference=request.data.get('extra_curricullums_preference')
            employment_preference =request.data.get('employment_preference')
            personalinterest_preference=request.data.get('personalinterest_preference')
            

            #Saving to database
            lead = User_Details.objects.create(name=name, details = details, qualification=qualification,extra_curricullums=extra_curricullums,employment=employment,personalinterest=personalinterest,qualification_preference=qualification_preference,extra_curricullums_preference=extra_curricullums_preference,employment_preference=employment_preference,personalinterest_preference=personalinterest_preference)
            lead.save()   #change name=models.OneToOneField(User)

            serializer = User_Details_Serializer(data=lead)
            if serializer.is_valid():
                serializer.save()
                #return Response(serializer.data)
            #else:
                #return Response(serializer.errors)
            

            #Sending Email to client
            #body = "Name: " +  name + "\n" + "details:"
            #email = EmailMessage('New Appointment Request', body, to=[''])
            #email.send()
            #messages.success(request, 'Thank you for registering')
            return HttpResponse("Form Successfully Submitted, Next Step --> Algorithm to be made")
        else:
            form=UserPreference()
            context={'form':form}
            return render(request,'counselling/user_preference.html',context)

@api_view(['GET', 'POST'])
def counsellors_register(request):
    #log.debug("Got user-register request. Data:%s", request.data)

    if request.method == 'GET':
        return render(request, 'counselling/counsellors_register.html', {})

    if request.method == 'POST':
        if(True):
            ret_val = {
                'data': None,
                'message': None,
                'status': None
            }

        if 'email' not in request.data or 'password' not in request.data:
            ret_status = status.HTTP_400_BAD_REQUEST
            ret_val["status"] = ret_status
            ret_val["message"] = "Required fields not found."
        else:
            email = request.data.get('email')
            password = request.data.get('password')

            # Check if email is already registered
            user = User.objects(email=email).first()

            if user is not None:
                ret_status = status.HTTP_200_OK
                ret_val["status"] = CustomStatus.EMAIL_ALREADY_REGISTERED
                ret_val["message"] = "Email already registered."
            else:
            
                user = User.objects.create(email=email,password=password)
                user.firstName = request.data.get('firstName');
                user.lastName = request.data.get('lastName');
                user.accessControl.isActivated = True
                user.accessControl.activationDate = TimeUtils.get_epoch_ms()

                #user.regDetails = RegistrationDetails()
                #user.regDetails.initialize(request.data.get('regDetails'))

                if 'gender' in request.data:
                    user.gender = request.data.get('gender')

                user.roles=UserRoles
                
                user.roles.jobCouncillor=JobCouncillor()
                #user.roles.jobCouncillor.role ="JOB_COUNCILLOR"
                user.roles.jobCouncillor.location=request.data.get('location')
                user.roles.jobCouncillor.exp=request.data.get('exp')
                user.roles.jobCouncillor.yearestb=request.data.get('yearestb')
                user.roles.jobCouncillor.examples=request.data.get('examples')
                user.roles.jobCouncillor.funcArea=request.data.get('funcArea')
                user.save()
                

                org=Organization_Details.objects.create(name=user.firstName,details=user)
                org.save()

                # send_mail("Welcome to MeraHunar",
                #           "Click on this link to activate your account: http://52.27.158.73/activate?email=" +
                #           email + "&activationId=" + user.accessControl.activationId, email)

                ret_status = status.HTTP_200_OK
                ret_val["status"] = ret_status
                ret_val["message"] = "Saved Successfully"

        return Response(data=ret_val, status=ret_status)

@api_view(['GET', 'POST'])
def freelancers_register(request):
    #log.debug("Got user-register request. Data:%s", request.data)

    if request.method == 'GET':
        return render(request, 'counselling/freelancers_register.html', {})

    if request.method == 'POST':
        if(True):
            ret_val = {
                'data': None,
                'message': None,
                'status': None
            }

        if 'email' not in request.data or 'password' not in request.data:
            ret_status = status.HTTP_400_BAD_REQUEST
            ret_val["status"] = ret_status
            ret_val["message"] = "Required fields not found."
        else:
            email = request.data.get('email')
            password = request.data.get('password')

            # Check if email is already registered
            user = User.objects(email=email).first()

            if user is not None:
                ret_status = status.HTTP_200_OK
                ret_val["status"] = CustomStatus.EMAIL_ALREADY_REGISTERED
                ret_val["message"] = "Email already registered."
            else:
            
                user = User.objects.create(email=email,password=password)
                user.firstName = request.data.get('firstName');
                user.lastName = request.data.get('lastName');
                user.accessControl.isActivated = True
                user.accessControl.activationDate = TimeUtils.get_epoch_ms()

                #user.regDetails = RegistrationDetails()
                #user.regDetails.initialize(request.data.get('regDetails'))

                if 'gender' in request.data:
                    user.gender = request.data.get('gender')

                user.roles=UserRoles()
                
                user.roles.freelancer=Freelancer()
                user.roles.jobCouncillor.title =request.data.get('lastName');
                user.roles.jobCouncillor.dob=request.data.get('dob')
                user.roles.jobCouncillor.Exp=request.data.get('exp')
                user.roles.jobCouncillor.funcArea=request.data.get('funcArea')
                user.roles.jobCouncillor.examples=request.data.get('examples')
                user.roles.jobCouncillor.jobRole=request.data.get('jobRole')
                user.save()
                

                ind=Individual_Details.objects.create(name=user.firstName,details=user)
                ind.save()

                # send_mail("Welcome to MeraHunar",
                #           "Click on this link to activate your account: http://52.27.158.73/activate?email=" +
                #           email + "&activationId=" + user.accessControl.activationId, email)

                ret_status = status.HTTP_200_OK
                ret_val["status"] = ret_status
                ret_val["message"] = "Saved Successfully"

        return Response(data=ret_val, status=ret_status)

@api_view(['GET'])
def OrganizationSearchBy_Location(request,location):
    if request.method == 'GET':
        organizations=User.objects(roles__jobCouncillor__location=location)###############CAn this be done directly like this?????
        context={'organizations':organizations}
        return render(request,'counselling/organizationdetails.html',context)

@api_view(['GET'])
def OrganizationSearchBy_Year(request,year1,year2):
    if request.method == 'GET':
        organizations=User.objects(Q(roles__jobCouncillor__exp__gt=year1) & Q(roles__jobCouncillor__exp__lte=year2))###############CAn this be done directly like this?????
        context={'organizations':organizations}
        return render(request,'counselling/organizationdetails.html',context)

@api_view(['GET'])
def OrganizationSearchBy_Field(request,field):
    if request.method == 'GET':
        organizations=User.objects(roles__jobCouncillor__funcArea=field)###############CAn this be done directly like this?????
        context={'organizations':organizations}
        return render(request,'counselling/organizationdetails.html',context)

@api_view(['GET'])
def FreelancerSearchBy_JobRoles(request,jobrole):
    if request.method == 'GET':
        organizations=User.objects(roles__freelancer__jobRole=jobrole)###############CAn this be done directly like this?????
        context={'organizations':organizations}
        return render(request,'counselling/freelancerdetails.html',context)

@api_view(['GET'])
def FreelancerSearchBy_Exp(request,exp1,exp2):
    if request.method == 'GET':
        organizations=User.objects(Q(roles__freelancer__Exp__gt=exp1) & Q(roles__freelancer__Exp__lte=exp2))###############CAn this be done directly like this?????
        context={'organizations':organizations}
        return render(request,'counselling/freelancerdetails.html',context)

@api_view(['GET'])
def FreelancerSearchBy_Field(request,field):
    if request.method == 'GET':
        organizations=User.objects(roles__freelancer__funcArea=field)###############CAn this be done directly like this?????
        context={'organizations':organizations}
        return render(request,'counselling/freelancerdetails.html',context)

            
@api_view(['GET'])
def get_all_organization(request):
    if request.method == 'GET':
        org=User.objects(roles__jobCouncillor__exists=True)
        context={'organizations':org}
        return render(request,'counselling/organizationdetails.html',context)

@api_view(['GET'])
def get_all_freelancer(request):
    if request.method == 'GET':
        org=User.objects(roles__freelancer__exists=True)
        context={'organizations':org}
        return render(request,'counselling/freelancerdetails.html',context)

@api_view(['GET'])
def get_single_organization(request,pk):
    if request.method == 'GET':
        org=User.objects(id=pk).first()##############################################
        #org = JobCouncillors.objects.get(pk=pk)
        organization=Organization_Details.objects(details=org).first()
        comments = Comment_Organization.objects(attribute=organization)
        #form=CommentFormOrganization()
        #serializer = User_Details_Serializer(data=organization)
        #if serializer.is_valid():
        #        serializer.save()
        context={'organization':organization,'comments':comments}
        return render(request,'counselling/individualorganization.html',context)   

@api_view(['GET'])
def get_single_freelancer(request,pk):
    if request.method == 'GET':
        org=User.objects(id=pk).first()##############################################
        #org = JobCouncillors.objects.get(pk=pk)
        organization=Individual_Details.objects(details=org).first()
        comments = Comment_Individual.objects(attribute=organization)
        #form=CommentFormOrganization()
        #serializer = User_Details_Serializer(data=organization)
        #if serializer.is_valid():
        #        serializer.save()
        context={'organization':organization,'comments':comments}
        return render(request,'counselling/individualfreelancer.html',context)     

@api_view(['POST'])
def add_comment_organization(request,pk):
    if request.method == 'POST':
        #CommentDetail = CommentFormOrganization(request.POST)
        if(True):
        #if UserDetail.is_valid():
            email=request.session.get('email')
            by=User.objects(email=email).first()##################How to identify the user
            attribute=Organization_Details.objects(id=pk).first()
            p = request.POST
            comment=p['comment']
            ranking=p['ranking']
            #Saving to database
            comment = Comment_Organization.objects.create(by=by,comment=comment,attribute=attribute)
            if(ranking):
                comment.ranking=ranking
            comment.save() 
    return HttpResponse("Successfully add_comment")

@api_view(['GET'])
def get_freelancer_blog(request,pk):
    if request.method == 'GET':
        #org=User.objects(id=pk).first()##############################################
        #org = JobCouncillors.objects.get(pk=pk)
        organization=Individual_Details.objects(id=pk).first()
        blog=Blog.objects(of=organization).first()
        qestions=Question.objects(attribute=blog)
        answers=[]
        for i,qestion in enumerate(qestions):
            if(Answer.objects(attribute=qestion)):
                answers.append(Answer.objects(attribute=qestion))
            else:
                answers.append([])

        email = request.session.get('email')############################################################################Ask
        details=User.objects(email=email).first()
        role=User.objects(email=email).first().roles

        context={'organization':organization,'blog':blog,'qestions':qestions,'answers':answers,'role':role}
        return render(request,'counselling/individualfreelancerbog.html',context)

@api_view(['POST'])
def add_blog_qestion(request,pk):####here pk is id of blog
    if request.method == 'POST':
        if(True):
            email=request.session.get('email')
            by=User.objects(email=email).first()##################How to identify the user
            #organization=Individual_Details.objects(id=pk).first()
            attribute=Blog.objects(id=pk).first()
            p = request.POST
            qestion=p['qestion']
            
            #Saving to database
            comment = Question.objects.create(by=by,qes=qestion,attribute=attribute)
            comment.save() 
    return HttpResponse("Successfully added Qestion")

@api_view(['POST'])
def add_blog_qestion(request,pk):
    if request.method == 'POST':
        if(True):
            email=request.session.get('email')
            user=User.objects(email=email).first()##################How to identify the user
            organization=Individual_Details.objects(details=user).first()
            attribute=Qestion.objects(id=pk).first()
            p = request.POST
            qestion=p['answer']
            
            #Saving to database
            comment = Answer.objects.create(by=organization,ans=answer,attribute=attribute)
            comment.save() 
    return HttpResponse("Successfully added Answer")

        



# Create your views here.
