
from django.shortcuts import render,redirect
from django.contrib.auth import logout,login
from django.contrib import messages
from hr.models import leave,salaryemp
from django.contrib.auth.models import auth,User
from adminpage.models import addemployee,announcement
from marketing.models import Emp_Quot,client
from .forms import FileForm



# Create your views here.


def view_leavetech(request,Employee_id):
    if request.method=='GET':

        employees =addemployee.objects.filter(Employee_id=Employee_id)
        leaves=leave.objects.filter(branch='Technical')
        return render(request, "view_leavetech.html", {'leaves':leaves,'employees':employees})

def techportal(request,username):
    context = {'employees': addemployee.objects.filter(username=username)}

    return render(request,'techportal.html',context)


def logout(request,Employee_id):
    auth.logout(request)
    return redirect('emplogin')

def view_tech(request,Employee_id):
    context = {'employees': addemployee.objects.filter(Employee_id=Employee_id)}
    return render(request, "view_tech.html", context)
def view_annountech(request,Employee_id):
   
    if request.method=='GET':

        employees =addemployee.objects.filter(Employee_id=Employee_id)
        announces=announcement.objects.filter(announce_to='All')| announcement.objects.filter(announce_to='Technical')
        return render(request, "view_annountech.html", {'announces':announces,'employees':employees})

def new_annountech(request,Employee_id):
   
    if request.method=='GET':

        employees =addemployee.objects.filter(Employee_id=Employee_id)
        announces=(announcement.objects.filter(announce_to='Technical')| announcement.objects.filter(announce_to='All')).order_by('-date')[:3]
        return render(request, "new_annountech.html", {'announces':announces,'employees':employees})



def leave_requesttech(request,Employee_id):
 
    if request.method == "GET":
        employees =addemployee.objects.filter(Employee_id=Employee_id)

        return render(request, "leave_requesttech.html",{'employees':employees})
    else:
       
        from_date=request.POST.get('from_date')
        to_date=request.POST.get('to_date')
        numdays=request.POST['numdays']
        leave_type=request.POST['leave_type']
        reason=request.POST['reason']
        

        employees =addemployee.objects.filter(Employee_id=Employee_id)
        for employee in employees:
            emp_name=employee.full_name
            emp_id=employee.Employee_id
            desgn=employee.designation
            branch=employee.dept
        
        user=leave.objects.create(status='Pending',from_date=from_date,to_date=to_date,emp_id=emp_id,emp_name=emp_name,desgn=desgn,branch=branch,numdays=numdays,leave_type=leave_type,reason=reason)
        user.save()

        return redirect('leave_requesttech',Employee_id=Employee_id)


def Salarytech(request,Employee_id):
    sala=salaryemp.objects.filter(emid=Employee_id).order_by("-month")
    employees =addemployee.objects.filter(Employee_id=Employee_id)
    return render(request,'Salarytech.html',{'employees':employees,'sala':sala})


def newprotech(request,Employee_id):
   
    employees =addemployee.objects.filter(Employee_id=Employee_id)
  
    e=Emp_Quot.objects.filter(accept='0',project_status='Ongoing') | Emp_Quot.objects.filter(accept='',project_status='Ongoing')
    return render(request,'newprotech.html',{'employees':employees,'e':e})


def assignedproject(request,Employee_id):
    e=Emp_Quot.objects.filter(accept='Accepted',project_status='Ongoing')  | Emp_Quot.objects.filter(accept='Accepted',project_status='Completed')
    print(e)
    employees =addemployee.objects.filter(Employee_id=Employee_id)
    return render(request,'assignedproject.html',{'employees':employees,'e':e})

def accept(request,id,Employee_id):
   
    employees =addemployee.objects.filter(Employee_id=Employee_id)
    Emp_Quot.objects.filter(id=id).update(accept='Accepted')
    e=Emp_Quot.objects.filter(accept='0',project_status='Ongoing') | Emp_Quot.objects.filter(accept='',project_status='Ongoing')
    return render(request,'newprotech.html',{'employees':employees,'e':e})


def files(request,id,Employee_id):

    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            m = Emp_Quot.objects.get(id=id)
            print('hi')
            m.source_code = form.cleaned_data['source_code']
            m.save()
            print('Hello')
            Emp_Quot.objects.filter(id=id).update(project_status='Completed')
            e=Emp_Quot.objects.filter(accept='Accepted',project_status='Ongoing') | Emp_Quot.objects.filter(accept='Accepted',project_status='Ongoing')
   
            employees =addemployee.objects.filter(Employee_id=Employee_id)
            return redirect('assignedproject',Employee_id=Employee_id)

            
        else:
            print("not valid")
            e=Emp_Quot.objects.filter(accept='Accepted',project_status='Ongoing')| Emp_Quot.objects.filter(accept='Accepted',project_status='Ongoing')
   
            employees =addemployee.objects.filter(Employee_id=Employee_id)
            return render(request,'assignedproject.html',{'employees':employees,'e':e})

    