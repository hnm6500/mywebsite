from django.shortcuts import render

# Create your views here.
from django.template import loader
from .models import PersonalInformation,Myobjective,myprojects
# Create your views here.
from django.http import HttpResponse
# Create your views here.
from django.core.files import File
from .models import Messages
from Profile.forms import CommentForm
from django.views.generic.edit import CreateView

def show_profile(request):
    person = PersonalInformation.objects.all()
    template = loader.get_template('Profile/myinfo.html')
    context = {
        'person':person,
    }
    return HttpResponse(template.render(context,request))

def homepage(request):
    person = PersonalInformation.objects.all()
    template = loader.get_template('Profile/homepage.html')
    context = {
        'person':person,
    }
    return HttpResponse(template.render(context,request))

def projectdetails(request):
    person=Myobjective.objects.all()
    template=loader.get_template('Profile/ProjectsDetail.html')
    context={'person':person,}
    return HttpResponse(template.render(context,request))

def detail1(request):
    person=Myobjective.objects.all()
    template=loader.get_template('Profile/detail1.html')
    context={'person':person,}
    return HttpResponse(template.render(context,request))
def detail2(request):
    person=Myobjective.objects.all()
    template=loader.get_template('Profile/detail2.html')
    context={'person':person,}
    return HttpResponse(template.render(context,request))
def detail3(request):
    person=Myobjective.objects.all()
    template=loader.get_template('Profile/detail3.html')
    context={'person':person,}
    return HttpResponse(template.render(context,request))
def detail4(request):
    person=Myobjective.objects.all()
    template=loader.get_template('Profile/detail4.html')
    context={'person':person,}
    return HttpResponse(template.render(context,request))
def detail5(request):
    person=Myobjective.objects.all()
    template=loader.get_template('Profile/detail5.html')
    context={'person':person,}
    return HttpResponse(template.render(context,request))
def detail6(request):
    person=Myobjective.objects.all()
    template=loader.get_template('Profile/detail6.html')
    context={'person':person,}
    return HttpResponse(template.render(context,request))
def detail7(request):
    person=Myobjective.objects.all()
    template=loader.get_template('Profile/detail7.html')
    context={'person':person,}
    return HttpResponse(template.render(context,request))

def showfile(request):
    file = myprojects.objects.all()
    template=loader.get_template('Profile/detail6.html')
    context={'file':file}
    return HttpResponse(template.render(context,request))





def get_message(request):


   if request.method == 'POST':
       form= CommentForm(request.POST)


       if form.is_valid():
           Name=request.POST.get('Name','')
           body=request.POST.get('body','')
           Email=request.POST.get('Email','')
           message1=Messages(Name=Name,body=body,Email=Email)
           message1.save()

           return HttpResponse('Message sent!')
   else:
           form = CommentForm()

   return render(request, 'Profile/index.html', {'form': form})

