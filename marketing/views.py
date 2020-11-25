from django.shortcuts import render,redirect
from django.contrib.auth import logout,login
from django.contrib import messages
from django.contrib.auth.models import auth,User
from hr.models import leave,salaryemp
from .forms import ClientForm
import datetime 
from datetime import date
from adminpage.models import addemployee,addservices,discount
from .models import client,Emp_Quot,services_quot
from adminpage.models import addemployee,announcement



# Create your views here.


def view_leavemar(request,Employee_id):
    if request.method=='GET':

        employees =addemployee.objects.filter(Employee_id=Employee_id)
        leaves=leave.objects.filter(branch='Marketing')
        return render(request, "view_leavemar.html", {'leaves':leaves,'employees':employees})

def marportal(request,username):
    context = {'employees': addemployee.objects.filter(username=username)}

    return render(request,'marportal.html',context)


def logout(request,Employee_id):
    auth.logout(request)
    return redirect('emplogin')

def view_mar(request,Employee_id):
    context = {'employees': addemployee.objects.filter(Employee_id=Employee_id)}
    return render(request, "view_mar.html", context)

def view_announmar(request,Employee_id):
   
    if request.method=='GET':

        employees =addemployee.objects.filter(Employee_id=Employee_id)
        announces=announcement.objects.filter(announce_to='All')|announcement.objects.filter(announce_to='Marketing')
        return render(request, "view_announmar.html", {'announces':announces,'employees':employees})

def new_announmar(request,Employee_id):
   
    if request.method=='GET':

        employees =addemployee.objects.filter(Employee_id=Employee_id)
        announces=(announcement.objects.filter(announce_to='Marketing')|announcement.objects.filter(announce_to='All')).order_by('-date')[:3]
        return render(request, "new_announmar.html", {'announces':announces,'employees':employees})


def leave_requestmar(request,Employee_id):
 
    if request.method == "GET":
        employees =addemployee.objects.filter(Employee_id=Employee_id)

        return render(request, "leave_requestmar.html",{'employees':employees})
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

        return redirect('leave_requestmar',Employee_id=Employee_id)

def Salarymar(request,Employee_id):
    sala=salaryemp.objects.filter(emid=Employee_id).order_by("-month")
    employees =addemployee.objects.filter(Employee_id=Employee_id)
    return render(request,'Salarymar.html',{'employees':employees,'sala':sala})




def adminportal(request):

    return render(request,'adminportal.html')

def addclient(request,Employee_id):
    if(request.method=='POST'):
        id=len(client.objects.all())+1
        clientid='CL' +str(id)
        clientname= request.POST['clientname']
        client_address= request.POST['client_address']
        company_name= request.POST['company_name']
        contact= request.POST['contact']
        alcontact= request.POST['alcontact']
        company_email= request.POST['company_email']
        meeting= request.POST['meeting']
        remarks= request.POST['remarks']
        status= request.POST['status']
        employees =addemployee.objects.filter(Employee_id=Employee_id)
       
        for i in employees:
            empname=i.full_name  
            empid=i.Employee_id
      
        if not client.objects.filter(clientname=clientname).exists():
            user=client.objects.create(clientid=clientid,empid=empid,company_email=company_email,empname=empname,status=status,clientname=clientname,client_address=client_address,meeting=meeting,company_name=company_name,contact=contact,remarks=remarks,alcontact=alcontact)
            user.save()

        else:
            messages.info(request,'User Exists')
        return redirect('addclient',Employee_id=Employee_id)

    else:
        employees =addemployee.objects.filter(Employee_id=Employee_id)
        id=len(client.objects.all())+1
        eid='CL' +str(id)
    
        return render(request,'addclient.html',{'clientid':eid,'employees':employees})

    
def client_form(request, id=0):
    if request.method == "GET":
        employees =client.objects.filter(pk=id)
        print(employees)
        for i in employees:
            em=i.empid
     
        employees=addemployee.objects.filter(Employee_id=em)
        if id == 0:
            form = ClientForm()
        else:
            employee = client.objects.get(pk=id)
            form = ClientForm(instance=employee)
        return render(request, "client_form.html", {'form': form,'employees':employees})
    else:
        employee = client.objects.get(pk=id)
        employees =client.objects.filter(pk=id)
        for i in employees:
            em=i.empid
      
        employees=addemployee.objects.filter(Employee_id=em)
        for i in employees:
            ids=i.id
        form = ClientForm(request.POST,instance= employee)
       
        if form.is_valid():
            form.save()
            print('save')
            return redirect('view_client',id=ids)
        else:
            return redirect('view_client',id=id)




def view_client(request,id):
    employees =addemployee.objects.filter(id=id)
    openclients= client.objects.filter(status='Opened')
    closeclients= client.objects.filter(status='Closed')
    return render(request, "view_client.html", {'openclients':openclients,'closeclients':closeclients,'employees':employees})


def quotation(request,clientid):
    employees =client.objects.filter(clientid=clientid)
    id=len( Emp_Quot.objects.all())+1
    qid='QUO' +str(id)
    date1=datetime.datetime.today()
    date=datetime.datetime.today().strftime ('%d-%b-%Y')
    for i in employees:
        category=i.meeting
        empname=i.empname
        remarks=i.remarks
    if(services_quot.objects.filter(clientid=clientid).exists()):
        subtotal=0
        discount=0
        tax_percent=0
        ser=services_quot.objects.filter(clientid=clientid)
        for i in ser:
            category=i.category
            subtotal+=int(i.total)
            quotation_id=i.quotation_id
            discount+=int(i.discount)
            tax_percent+=int(i.tax_percent)
        e=client.objects.filter(clientid=clientid)
        for i in e:
            client_name=i.company_name
        discount=(discount*subtotal)/100
        tax_percent=(tax_percent*subtotal)/100
        total=subtotal-discount+tax_percent
        print(total)
        if( Emp_Quot.objects.filter(quotation_id=quotation_id,clientid=clientid).exists()):
            Emp_Quot.objects.filter(quotation_id=quotation_id,clientid=clientid).update(subtotal=subtotal,discount=discount,tax=tax_percent,total=total)
        else:
            Emp_Quot.objects.create(quotation_id=quotation_id,executive=empname,work=False,second_payment_date=date1,third_payment_date=date1,remarks=remarks,category=category,client_name=client_name,clientid=clientid,first_payment_date=date1,subtotal=subtotal,discount=discount,tax=tax_percent,total=total)
        client.objects.filter(clientid=clientid).update(total=total)
        quotate=Emp_Quot.objects.filter(quotation_id=quotation_id)
        return render(request, "quotation.html", {'quotation_id':quotation_id,'clientid':clientid,'date':date,'employees':employees,'quotate':quotate,'ser':ser})
    else:
        return render(request, "quotation.html", {'quotation_id':qid,'clientid':clientid,'date':date,'employees':employees})
        



   

def quot(request,quotation_id,clientid):
    employees =client.objects.filter(clientid=clientid)
    for employee in employees:
        category=employee.meeting


 
    service_name= request.POST['service_name']
    no_of_units= request.POST['no_of_units']
    tax= request.POST['tax']
    s=addservices.objects.filter(category=category,service_name=service_name)
    for i in s:
        service_id=i.service_id
        cost=i.cost
        technology=i.technology
    if(discount.objects.filter(service_id=service_id).exists()):
        s= discount.objects.filter(service_id=service_id)
        for i in s:
            r=str(i.from_date)
            r=r.split("-")
            print(r)
            d1=datetime.date(int(r[0]),int(r[1]),int(r[2]))
            m=str(i.to_date)
            m=m.split("-")
            print(m)
            d3=datetime.date(int(m[0]),int(m[1]),int(m[2]))
    
            d2=datetime.datetime.today()
            d2=str(d2)
            d2=d2.split(' ')
            q=d2[0].split('-')
            print(q)
            d2=datetime.date(int(q[0]),int(q[1]),int(q[2]))
            print(d2)
            if d1 < d2 < d3:
                print("BETWEEN!")
                discounts=i.dis_per
            else:
                discounts=0
    else:
        discounts=0
            
    total=int(no_of_units)*int(cost)
    if(services_quot.objects.filter(service_name=service_name,category=category,clientid=clientid,quotation_id=quotation_id).exists()):
        pass
    else:
        services_quot.objects.create(clientid=clientid,technology=technology,total=total,discount=discounts,quotation_id=quotation_id,tax_percent=tax,no_of_units=no_of_units,category=category,service_id=service_id,service_name=service_name)
    
    date=datetime.datetime.today().strftime ('%d-%b-%Y')
    return redirect('quotation',clientid=clientid)

def submit(request,clientid):
    print('hello',clientid)
    Emp_Quot.objects.filter(clientid=clientid).update(status='Generated')
    client.objects.filter(clientid=clientid).update(quotation='Generated')
    

    c=client.objects.filter(clientid=clientid)
    print(c)
    for i in c:
        empid=i.empid
    emp=addemployee.objects.filter(Employee_id=empid)
    for i in emp:
        id=i.id
    
    
    return redirect('view_client',id=id)

def  viewquot(request,Employee_id):
    employees =addemployee.objects.filter(Employee_id=Employee_id)
    generate= Emp_Quot.objects.filter(status='Generated')
    accept= Emp_Quot.objects.filter(status='Accepted')
    not_accept= Emp_Quot.objects.filter(status='Not Accepted')
    return render(request, "viewquot.html", {'generate':generate,'accept':accept,'notaccept':not_accept,'employees':employees})

def view(request,clientid):
    employees =client.objects.filter(clientid=clientid)
    ser=services_quot.objects.filter(clientid=clientid)
    for i in ser:
        quotation_id=i.quotation_id
    quotate=Emp_Quot.objects.filter(quotation_id=quotation_id)
    for i in quotate:
        date=i.date
    return render(request, "view.html", {'quotation_id':quotation_id,'clientid':clientid,'date':date,'employees':employees,'quotate':quotate,'ser':ser})

def quotdown(request,clientid):
    employees =client.objects.filter(clientid=clientid)
    ser=services_quot.objects.filter(clientid=clientid)
    for i in ser:
        quotation_id=i.quotation_id
    quotate=Emp_Quot.objects.filter(quotation_id=quotation_id)
    for i in quotate:
        date=i.date
    return render(request, "quotdown.html", {'quotation_id':quotation_id,'clientid':clientid,'date':date,'employees':employees,'quotate':quotate,'ser':ser})
  
def amount(request,Employee_id):
    quotation_id=request.POST['quotation_id']
    status=request.POST['status1']
    client_deadline=request.POST['client_deadline1']
    first_payment_date=request.POST['first_payment_date']
    first_amt=request.POST['amount']
    reason=request.POST['reason']
    
    if (status=='Accepted'):
        Emp_Quot.objects.filter(quotation_id=quotation_id).update( status='Accepted',client_deadline=client_deadline,first_amt=first_amt,first_payment_date=first_payment_date)
    elif( status=='Not Accepted'):
        Emp_Quot.objects.filter(quotation_id=quotation_id).update( status='Not Accepted',reason=reason)
    else:
        Emp_Quot.objects.filter(quotation_id=quotation_id).update( status='Generated')
    
    employees =addemployee.objects.filter(Employee_id=Employee_id)
    generate= Emp_Quot.objects.filter(status='Generated')
    accept= Emp_Quot.objects.filter(status='Accepted')
    not_accept= Emp_Quot.objects.filter(status='Not Accepted')
    return render(request, "viewquot.html", {'generate':generate,'accept':accept,'notaccept':not_accept,'employees':employees})





def payment(request,Employee_id):
    r=Emp_Quot.objects.filter(status='Accepted')
    for i in r:
        print(i.second_amt)
        if i.second_amt==0:
            pay=True
        else:
            pay=False
   
    employees =addemployee.objects.filter(Employee_id=Employee_id)
    return render(request,'payment.html',{'employees':employees,'r':r})


def quotview(request,clientid):
    employees =client.objects.filter(clientid=clientid)
    ser=services_quot.objects.filter(clientid=clientid)
    for i in ser:
        quotation_id=i.quotation_id
    quotate=Emp_Quot.objects.filter(quotation_id=quotation_id)
    for i in quotate:
        date=i.date
    return render(request, "quotview.html", {'quotation_id':quotation_id,'clientid':clientid,'date':date,'employees':employees,'quotate':quotate,'ser':ser})
  