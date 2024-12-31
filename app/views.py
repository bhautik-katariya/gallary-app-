from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
# from django.contrib.auth import get_user_model

# user =  get_user_model()

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = User_register(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = User_register()
    return render(request,'register.html',{'form':form})

def login_view(request):
    if request.method == "POST":
        name = request.POST.get('username')
        passwd = request.POST.get('pass')
        user = authenticate(request, username=name, password=passwd)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            er_msg = "Failed!"
            return render(request,'login.html', {'error':er_msg})
    return render(request,'login.html')


def photo_list(request):
    photo = gallary.objects.filter(user = request.user)
    return render(request,'Home.html',{'photos':photo})

@login_required
def add(request):
    if request.method == "POST":
        form = gallaryphoto(request.POST,request.FILES)
        if form.is_valid():
            add = form.save(commit=False)
            add.user = request.user
            add.save()
            return redirect('list')
    else:
        form = gallaryphoto()
    return render(request,'add.html',{'form':form})

@login_required
def  update(request,photo_id):  
        pic = gallary.objects.get(id=photo_id, user=request.user)
        if request.method =="POST":
            form = gallaryphoto(request.POST,request.FILES,instance = pic)
            if form.is_valid():
                form.save()
                return redirect('list')
        else: 
            form = gallaryphoto(instance = pic)
        return render(request,'update.html',{'form':form})

@login_required
def delete(request,photo_id):
    pic = gallary.objects.filter(id=photo_id, user=request.user)
    if request.method == "POST":
        pic.delete()
        return redirect('list')
    return render(request,'delete.html',{'pic':pic})

# maillll setupppp system in djnago.....................................................

def mail_send(request):
    subject = request.session.get('subject')
    message=request.session.get('message')
    from_email=request.session.get('from_mail')
    recipient_list=request.session.get('to_mail')
    res  = send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=[recipient_list, ]
    )
    if res == 1:               
        msg = "Mail Sent Successfuly"  
    else:  
        msg = "Mail could not sent"  
    return HttpResponse(msg)   

def mail_setup(request):
    error=""
    if request.method == "POST":
        sub = request.POST.get('subject')
        mess = request.POST.get('message')
        from_mail = request.POST.get('from_mail')
        to_mail = request.POST.get('to_mail')
        print(f"Subject: {sub}, Message: {mess}, To Email: {to_mail}, from_mail: {from_mail}")
        if sub and mess and to_mail and from_mail:
            request.session['subject']= sub
            request.session['message']= mess
            request.session['from_mail']= from_mail
            request.session['to_mail']= to_mail
            return redirect('send_mail')
        else:
            error = 'All fields are required'
    return render(request,'mail.html', {'error':error})
    

