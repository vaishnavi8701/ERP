from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth,User
from adminpage.models import addemployee
from hr.models import OTP
from ERP.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
import random

def login(request):
    return render(request,'login.html')


def adlogin(request):
    if  (request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('adminportal')
        
        else:
            messages.info(request,'Invalid Username and Password!')
            #return HttpResponse('adlogin', messages='Invalid Username and Password!')
            return redirect('adlogin')
    else:
        return render(request,'adlogin.html')

def emplogin(request):
    if  (request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        if addemployee.objects.filter(username=username,password=password).exists():
            if addemployee.objects.filter(username=username,password=password,dept='Human Resource'):
                return redirect('hrportal',username=username)
            elif addemployee.objects.filter(username=username,password=password,dept='Finance'):
                return redirect('finportal',username=username)
            elif addemployee.objects.filter(username=username,password=password,dept='Technical'):
                return redirect('techportal',username=username)
            elif addemployee.objects.filter(username=username,password=password,dept='Marketing'):
                return redirect('marportal',username=username)

        else:
            messages.info(request,'Invalid Username and Password!')
            #return HttpResponse('adlogin', messages='Invalid Username and Password!')
            return redirect('emplogin')
    else:
        return render(request,'emplogin.html')

        
def forgotpass(request):
    if  (request.method=='POST'):
        pemail=request.POST['email']
        pemail=pemail.lower()
        print(pemail)
        if addemployee.objects.filter(pemail=pemail).exists():
            m=random.randrange(1000000, 100000, -2)
            OTP.objects.create(email=pemail,otp=m)
            subject = 'OTP Techvolt'
            message = "OTP: "+str(m)
            recepient = str(pemail)
            send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
            context=OTP.objects.last()
            content= {'last': context}
            return render(request,'otp.html',content)
        else:
            messages.info(request,'Invalid Email')
            return redirect('forgotpass')
    else:
        return render(request,'forgotpass.html')

def otp(request,id):
    context=OTP.objects.filter(id=id)
    if (request.method=='POST'):
        context=OTP.objects.filter(id=id)
    
        for i in context:
            email=i.email
            otp=i.otp
        otp1=int(otp)
       
        otp=request.POST['otp']
        otp=int(otp)
       
        if(otp==otp1):
            context=OTP.objects.last()
            content= {'last': context}
            
            return render(request,'resetpass.html',content)
        else:
            messages.info(request,"Invalid OTP try again")
            return redirect('forgotpass')
    else:
        return render(request,"otp.html",{'context':context})  
   
def resetpass(request,id):
    context=OTP.objects.filter(id=id)
    if (request.method=='POST'):
        context=OTP.objects.filter(id=id)
    
        for i in context:
            email=i.email
            
        
       
        password1=request.POST['password1']
        password2=request.POST['password2']
       
        print(password1)
        if(password1==password2):
            addemployee.objects.filter(pemail=email).update(password=password1)
            
            return redirect('emplogin')
        else:
            messages.info(request,"Password not matched!")
            return render(request,'resetpass.html',{'context':context})
            
    else:
        return render(request,"resetpass.html",{'context':context})  
