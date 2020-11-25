from django.shortcuts import render,redirect
from django.contrib.auth import logout,login
from django.contrib import messages
from django.contrib.auth.models import auth,User
from adminpage.models import addemployee,announcement
from . models import leave,salaryemp,salmonth
from ERP.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from adminpage.forms import announce,EmployeeForm
from datetime import date, datetime

# Create your views here.

def hrportal(request,username):
    context = {'employees': addemployee.objects.filter(username=username)}

    return render(request,'hrportal.html',context)


def logout(request,Employee_id):
    auth.logout(request)
    return redirect('emplogin')

def view_profile(request,Employee_id):
    context = {'employees': addemployee.objects.filter(Employee_id=Employee_id)}
    return render(request, "view_profile.html", context)



def new_announhr(request,Employee_id):
    id=0
    if request.method == "GET":
        employees =addemployee.objects.filter(Employee_id=Employee_id)
        
        if id == 0:
            form = announce()
        else:
            employee = announcement.objects.get(pk=id)
            form = announce(instance=employee)
        return render(request, "new_announhr.html",{'form':form,'employees':employees})
    else:
        
        if id == 0:
            form = announce(request.POST)

        else:
            employee = announcement.objects.get(pk=id)
            form = announce(request.POST,instance= employee)

        if form.is_valid():
            form.save()
        context=announcement.objects.last()

        announcement.objects.filter(id=context.pk).update(announce_by='HR')
        subject = 'New Announcement from Techvolt'
        s=announcement.objects.filter(id=context.pk)
        from_email='techvolt123@gmail.com'
        for i in s:
            message1=i.message
        
        message = "Welcome, "+'\n\n'+message1+'\n'+'\n'+"Thanks and Regards,"+'\n'+"HR, Techvolt."
        if(announcement.objects.filter(id=context.pk,announce_to='All')):
            recievers = []
            for user in addemployee.objects.all():
                recievers.append(user.pemail)
            send_mail(subject, message, from_email, recievers)
        elif(announcement.objects.filter(id=context.pk,announce_to='Technical')):
            recievers = []
            for user in addemployee.objects.filter(dept='Technical'):
                recievers.append(user.pemail)
            send_mail(subject, message, from_email, recievers)
        elif(announcement.objects.filter(id=context.pk,announce_to='Marketing')):
            recievers = []
            for user in addemployee.objects.filter(dept='Marketing'):
                recievers.append(user.pemail)
            send_mail(subject, message, from_email, recievers)
        elif(announcement.objects.filter(id=context.pk,announce_to='Finance')):
            recievers = []
            for user in addemployee.objects.filter(dept='Marketing'):
                recievers.append(user.pemail)
            send_mail(subject, message, from_email, recievers)
        elif(announcement.objects.filter(id=context.pk,announce_to='HR')):
            recievers = []
            for user in addemployee.objects.filter(dept='Human Resource'):
                recievers.append(user.pemail)
            send_mail(subject, message, from_email, recievers)
        
        return redirect('view_announhr',Employee_id=Employee_id)



def view_announhr(request,Employee_id):
    if request.method=='GET':

        employees =addemployee.objects.filter(Employee_id=Employee_id)
        announces=announcement.objects.all().order_by('-date')[:5]
        return render(request, "view_announhr.html", {'announces':announces,'employees':employees})


def view_leavehr(request,Employee_id):
    if request.method=='GET':

        employees =addemployee.objects.filter(Employee_id=Employee_id)
        leaves=leave.objects.filter(branch='Human Resource')
        return render(request, "view_leavehr.html", {'leaves':leaves,'employees':employees})

def view_approvehr(request,Employee_id):
    if request.method=='GET':

        employees =addemployee.objects.filter(Employee_id=Employee_id)
        leaves=leave.objects.filter(status='Accepted',branch='Finance')|leave.objects.filter(status='Accepted',branch='Marketing')|leave.objects.filter(status='Accepted',branch='Technical')
        leavesm=leave.objects.filter(status='Rejected',branch='Finance')|leave.objects.filter(status='Rejected',branch='Marketing')|leave.objects.filter(status='Rejected',branch='Technical')
        return render(request, "view_approvehr.html", {'leaves':leaves,'leavesm':leavesm,'employees':employees})


def new_approvehr(request,Employee_id):
    if request.method=='GET':

        employees =addemployee.objects.filter(Employee_id=Employee_id)
        leaves=leave.objects.filter(status='Pending',branch='Finance')|leave.objects.filter(status='Pending',branch='Marketing')|leave.objects.filter(status='Pending',branch='Technical')
        return render(request, "new_approvehr.html", {'leaves':leaves,'employees':employees})

def approvehr(request,emp_id,id):
    if request.method=='GET':
        leave.objects.filter(id=id).update(status='Accepted')
        employees =addemployee.objects.filter(Employee_id=emp_id)
        leaves=leave.objects.filter(status='Pending',branch='Finance')|leave.objects.filter(status='Pending',branch='Marketing')|leave.objects.filter(status='Pending',branch='Technical')
        return render(request, "new_approvehr.html", {'leaves':leaves,'employees':employees})

def rejecthr(request,emp_id,id):
    if request.method=='GET':
        leave.objects.filter(id=id).update(status='Rejected')
        employees =addemployee.objects.filter(Employee_id=emp_id)
        leaves=leave.objects.filter(status='Pending',branch='Finance')|leave.objects.filter(status='Pending',branch='Marketing')|leave.objects.filter(status='Pending',branch='Technical')
        return render(request, "new_approvehr.html", {'leaves':leaves,'employees':employees})

def exist_emphr(request,id):
    employees =addemployee.objects.filter(pk=id)
    exist_emp= addemployee.objects.all()
    print(exist_emp)
    return render(request, "exist_emphr.html", {'exist_emp':exist_emp,'employees':employees})

def addemphr(request,Employee_id):
    empid=Employee_id
    
    if(request.method=='POST'):
        empid=Employee_id
        employees =addemployee.objects.filter(Employee_id=Employee_id)
        
        id=len(addemployee.objects.all())+1
        eid='EM' +str(id)
        Employee_id=eid
        username = eid
        image='pics/person.png'
        full_name =  request.POST['full_name']
        password =  eid +full_name[:4]
        father_name =  request.POST['father_name']
        contact =  request.POST['contact']
        aadhar =  request.POST['aadhar']
        pan =  request.POST['pan']
        whrs =  request.POST['whrs']
        oemail =  request.POST['oemail']
        pemail =  request.POST['pemail']
        designation =  request.POST['designation']
        dept =  request.POST['dept']
        Gender = request.POST['Gender']
        doj =  request.POST['doj']
        address =  request.POST['address']
        job_loc =  request.POST['job_loc']
        bank_name =  request.POST['bank_name']
        ba_no =  request.POST['ba_no']
        pfno =  request.POST['pfno']
        salary =  request.POST['salary']
        oemail=oemail.lower()
        pemail=pemail.lower()

        
        if not addemployee.objects.filter(oemail=oemail).exists():
            user=addemployee.objects.create(username=username,Employee_id=Employee_id,image=image,password=password,full_name=full_name,oemail=oemail,pemail=pemail,father_name=father_name,pan=pan,pfno=pfno,whrs=whrs,salary=salary,ba_no=ba_no,bank_name=bank_name,job_loc=job_loc,aadhar=aadhar,address=address,dept=dept,designation=designation,doj=doj,contact=contact,Gender=Gender)
            user.save()

        else:
            messages.info(request,'User Exists')
        return redirect('addemphr',Employee_id=Employee_id)

    else:
        employees =addemployee.objects.filter(Employee_id=Employee_id)
        id=len(addemployee.objects.all())+1
        eid='EM' +str(id)
        return render(request,'addemphr.html',{'empid':eid,'employees':employees})
    



def employee_form1(request,id=0):
    if request.method == "GET":
        employees =addemployee.objects.filter(pk=id)
        print(id)
        if id == 0:
            form = EmployeeForm()
        else:
            employee = addemployee.objects.get(pk=id)
            
            form = EmployeeForm(instance=employee)
        return render(request, "employee_form1.html", {'form': form,'employees':employees})
    else:
        employees = addemployee.objects.get(pk=id)
        form = EmployeeForm(request.POST,instance= employees)
        print(form)
        if form.is_valid():
            form.save()
        
            return redirect('exist_emphr',id=id)
        else:
            return redirect('exist_emphr',id=id)

def leave_requesthr(request,Employee_id):
 
    if request.method == "GET":
        employees =addemployee.objects.filter(Employee_id=Employee_id)

        return render(request, "leave_requesthr.html",{'employees':employees})
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

        return redirect('leave_requesthr',Employee_id=Employee_id)

def viewsalhr(request,Employee_id):
    Empoyee_id=request.POST.getlist('employee')
    Empoyee=request.POST.getlist('present_days')
    print(Empoyee_id,Empoyee)
    rt=salmonth.objects.all().last()
    st=rt.month
    r=str(st)
    y=r[5:7]
 
 
    exist_emp = addemployee.objects.filter(id__in=Empoyee_id)
    print(exist_emp)
    for i in exist_emp:
        m=i.dept
    print(m)
    qw=salaryemp.objects.filter(status='Generated') 
    l=[]
    for i in qw:
        v=str(i.date_of_generate)
        if(v[5:7]==r[5:7]):
           l.append(i.emid)
    exist = addemployee.objects.filter(dept=str(m))
    print(exist)
    qr=addemployee.objects.filter(dept=m) 
    print(l)
    print('qr',qr)
    l1=[]
    for i in qr:
        l1.append(i.Employee_id)
    print(l1)
    l2=list(set(l1)-set(l))
    print(l2)
    o=[]
    r= addemployee.objects.filter(Employee_id__in=l2)
    print(r)
    for i in r:
        o.append(int(i.id))
    q=[]
    print('o is',o)
    print(Empoyee)
    for i in Empoyee_id:
        i=int(i)
        if i in o:
            s=addemployee.objects.filter(id=i)
            print('hellow')
            for u in s:
                emp_name=u.full_name
                dept=u.dept
                acno=u.ba_no
                emid=u.Employee_id
                q.append(u.Employee_id)
                sal=u.salary
            working_days=30
            p=o.index(i)
            e=Empoyee[p]
            gross=((int(e)/30)*sal)
            pf=round(gross*0.4*0.12,3)
            esi=round(gross*0.4*0.0075,3)
            basic_pay=0.4*gross
            hra=0.5*basic_pay
            special_allowance=gross-basic_pay-hra
            month=rt.month
            gross=round(gross, 3)
            
            if(salaryemp.objects.filter(month=month,emid=emid).exists()):
                
                salaryemp.objects.filter(emid=emid).update(present_days=e,hra=hra,special_allowance=special_allowance,basic_pay=basic_pay,gross=gross,pf=pf,esi=esi)
            else:
               
                salaryemp.objects.create(present_days=e,month=month,acno=acno,emp_name=emp_name,dept=dept,sal=sal,emid=emid,working_days=working_days,hra=hra,special_allowance=special_allowance,basic_pay=basic_pay,gross=gross,pf=pf,esi=esi)
    
    sala = salaryemp.objects.filter(emid__in=q,month=rt.month) 
     
    employees= addemployee.objects.filter(Employee_id=Employee_id)

    return render(request, "viewsalhr.html", {'sala':sala,'employees':employees})

def gensal(request,Employee_id):
    employees =addemployee.objects.filter(Employee_id=Employee_id)
    if request.method=='POST':
        month=request.POST['month']
        dept=request.POST['dept']
        salmonth.objects.create(month=month,dept=dept)
      
        m=salaryemp.objects.filter(dept=dept)
        e=[]
        for i in m:
            date=i.month
            d=str(date)
            print(d)
            if(str(month)==d[:7]):
                if(i.status=='Generated' or i.status=='Paid'):
                    e.append(i.emid)
        
        exist_emp= addemployee.objects.filter(dept=dept)
        o=[]
        for i in exist_emp:
            o.append(i.Employee_id)
        emp=list(set(o) - set(e))
        print(emp)
        exist_emp= addemployee.objects.filter(dept=dept,Employee_id__in=emp)
        return render(request, "gensalhr.html", {'exist_emp':exist_emp,'employees':employees})
    else:
        return render(request,'gensal.html',{'employees':employees})


def salaryslip(request,Employee_id):

    Empoyee_id=request.POST.getlist('employee')
    Empoyee=request.POST.getlist('it')
    exist_emp = salaryemp.objects.filter(emid__in=Empoyee_id)
    r=[]
    for i in salaryemp.objects.filter(status=''):
        r.append(i.emid)
    for i in Empoyee_id:
        m=r.index(i)
        empsal=salaryemp.objects.filter(emid=i)
        for i in empsal:
            emid=i.emid
            gross=i.gross
            pf=i.pf
            esi=i.esi
        it=Empoyee[m]
        total_dedu=round(float(pf)+float(esi)+float(it),2)
        payable=round(float(gross)-total_dedu,2)
        status='Generated'
        salaryemp.objects.filter(emid=emid).update(it=it,total_dedu=total_dedu,payable=payable,status=status)

    sala=salaryemp.objects.all().order_by("-month")
    employees =addemployee.objects.filter(Employee_id=Employee_id)
    return render(request,'view_salaryhr.html',{'employees':employees,'sala':sala})

def view_salaryhr(request,Employee_id):
    sala=salaryemp.objects.all().order_by("-month")
    employees =addemployee.objects.filter(Employee_id=Employee_id)
    return render(request,'view_salaryhr.html',{'employees':employees,'sala':sala})


def Salaryhr(request,Employee_id):
    sala=salaryemp.objects.filter(emid=Employee_id).order_by("-month")
    employees =addemployee.objects.filter(Employee_id=Employee_id)
    return render(request,'Salaryhr.html',{'employees':employees,'sala':sala})

def salary_slip(request,id):
    sala=salaryemp.objects.filter(id=id)
    for i in sala:
        emp=i.emid
    employees =addemployee.objects.filter(Employee_id=emp)
    
    return render(request,'salary_slip.html',{'employees':employees,'sala':sala})

def salary_down(request,id):
    sala=salaryemp.objects.filter(id=id)
    for i in sala:
        emp=i.emid
    employees =addemployee.objects.filter(Employee_id=emp)
    
    return render(request,'salary_down.html',{'employees':employees,'sala':sala})
