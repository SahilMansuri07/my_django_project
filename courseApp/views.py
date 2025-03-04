from django.shortcuts import render
from .models import *
from .forms import *
from django import http

# Create your views here.
def registration(request):
    if request.method == 'POST':
        fm = UserRegisteration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            cpass = request.POST['cpass']
            if cpass != password:
                return http.HttpResponse("Confirm Password must be same as Password.")            
            else:
                try:
                    Registeration.objects.get(name=name)
                    return http.HttpResponse("username is already Exits.")
                except Registeration.DoesNotExist:
                    try:
                        Registeration.objects.get(email=email)
                        return http.HttpResponse("email is already Exits.")
                    except Registeration.DoesNotExist:
                        register = Registeration(name=name,email=email,password=password)
                        register.save()
                        return http.HttpResponseRedirect('/courseApp/login')
    fm = UserRegisteration()
    return render(request,'registeration.html',{'fm':fm})

def login(request):
    if request.method == 'POST':
        fm = LoginChecking(request.POST)
        if fm.is_valid():
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            try:
                user = Registeration.objects.get(email=email,password=password)
                request.session['s_name'] = email
                response = http.HttpResponseRedirect('/courseApp/courselist')
                response.set_cookie('c_name',user.name)
                return response
            except Registeration.DoesNotExist:
                return http.HttpResponse('Wrong email or password entered.')     
    fm = LoginChecking()
    return render(request,'login.html',{'fm':fm})

def courselist(request):
    s_name = request.session.get('s_name')
    c_name = request.COOKIES.get('c_name')
    if c_name is None and s_name is None:
        return http.HttpResponseRedirect('/courseApp/login')
    cou = Course.objects.all()
    return render(request,'courselist.html',{'name':c_name,'cou':cou})

def logout(request):
    del request.session['s_name']
    response = http.HttpResponseRedirect('/courseApp/login')
    response.delete_cookie('c_name')
    return response

def subject(request,id):
    s_name = request.session.get('s_name')
    c_name = request.COOKIES.get('c_name')
    if c_name is None and s_name is None:
        return http.HttpResponseRedirect('/courseApp/login')
    elif request.method == 'POST':
        cid = request.POST['cid']
        regnm = Registeration.objects.get(name=c_name)
        regid = Registeration.objects.get(id=regnm.id)
        couid = Course.objects.get(id=cid)
        try:
            Enrollment.objects.get(registeration=regid,course=couid)
            return http.HttpResponseRedirect('/courseApp/enrollment')
        except Enrollment.DoesNotExist:
            enroll = Enrollment(registeration=regid,course=couid)
            enroll.save()
            return http.HttpResponseRedirect('/courseApp/enrollment')
    cou = Course.objects.get(pk=id)
    sub = Subject.objects.filter(course=id)
    return render(request,'subject.html',{'name':c_name,'sub':sub,'cou':cou})

def addcourse(request):
    if request.method == 'POST':
        fm = AddCourse(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            description = request.POST['description']
            course = Course(name=name,description=description)
            course.save()
            return http.HttpResponseRedirect('/courseApp/addcourse')
    fm = AddCourse()
    return render(request,'addcourse.html',{'fm':fm})

def addsubject(request):
    if request.method == 'POST':
        fm = AddSubject(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            course = request.POST['course']
            c_id = Course.objects.get(id=course)
            sub = Subject(name=name,course=c_id)
            sub.save()
            return http.HttpResponseRedirect('/courseApp/addsubject')
    fm = AddSubject()
    cou = Course.objects.all()
    return render(request,'addsubject.html',{'fm':fm,'cou':cou})

def enrollment(request):
    s_name = request.session.get('s_name')
    c_name = request.COOKIES.get('c_name')
    if c_name is None and s_name is None:
        return http.HttpResponseRedirect('/courseApp/login')
    regnm = Registeration.objects.get(name=c_name)
    regid = Registeration.objects.get(id=regnm.id)
    en = Enrollment.objects.filter(registeration=regid)
    return render(request,'enrollment.html',{'en':en,'name':c_name})