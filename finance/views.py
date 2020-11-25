from django.shortcuts import render,redirect
from django.contrib.auth import logout,login
from django.contrib import messages
from django.contrib.auth.models import auth,User
from adminpage.models import addemployee,announcement
from hr.models import leave,salaryemp
import datetime
from .models import vendor,Receipt,taxpayment
from .forms import VendorForm
from marketing.models import Emp_Quot,client



# Create your views here.

def finportal(request,username):
    context = {'employees': addemployee.objects.filter(username=username)}

    return render(request,'finportal.html',context)


def logout(request,Employee_id):
    auth.logout(request)
    return redirect('emplogin')

def view_fin(request,Employee_id):
    context = {'employees': addemployee.objects.filter(Employee_id=Employee_id)}
    return render(request, "view_fin.html", context)


def view_announfin(request,Employee_id):
   
    if request.method=='GET':

        employees =addemployee.objects.filter(Employee_id=Employee_id)
        announces=announcement.objects.filter(announce_to='All')|announcement.objects.filter(announce_to='Finance')
        return render(request, "view_announfin.html", {'announces':announces,'employees':employees})

def new_announfin(request,Employee_id):
   
    if request.method=='GET':

        employees =addemployee.objects.filter(Employee_id=Employee_id)
        announces=(announcement.objects.filter(announce_to='Finance')|announcement.objects.filter(announce_to='All')).order_by('-date')[:3]
        return render(request, "new_announfin.html", {'announces':announces,'employees':employees})
    

def leave_requestfin(request,Employee_id):
 
    if request.method == "GET":
        employees =addemployee.objects.filter(Employee_id=Employee_id)

        return render(request, "leave_requestfin.html",{'employees':employees})
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

        return redirect('leave_requestfin',Employee_id=Employee_id)




def view_leavefin(request,Employee_id):
    if request.method=='GET':

        employees =addemployee.objects.filter(Employee_id=Employee_id)
        leaves=leave.objects.filter(branch='Finance')
        return render(request, "view_leavefin.html", {'leaves':leaves,'employees':employees})	

def Salaryfin(request,Employee_id):
    sala=salaryemp.objects.filter(emid=Employee_id).order_by("-month")
    employees =addemployee.objects.filter(Employee_id=Employee_id)
    return render(request,'Salaryfin.html',{'employees':employees,'sala':sala})

def emppayfin(request,Employee_id):
    employees =addemployee.objects.filter(Employee_id=Employee_id)
    return render(request,'emppayfin.html',{'employees':employees})


def pastpay(request,Employee_id):
    sala=salaryemp.objects.filter(status='Paid').order_by("-date_of_payment")
    employees =addemployee.objects.filter(Employee_id=Employee_id)
    return render(request,'pastpay.html',{'employees':employees,'sala':sala})

def emppayfin1(request,Employee_id):
    month=request.POST['month']
    salaryemp.objects.filter(month=month,status='Generated').update(status='p')
    sala=salaryemp.objects.filter(month=month,status='p')
    employees =addemployee.objects.filter(Employee_id=Employee_id)
 
    return render(request,'emppayfin1.html',{'employees':employees,'sala':sala})

def emppay(request,Employee_id):
    Empoyee=request.POST.getlist('employee')
    salaryemp.objects.filter(emid__in=Empoyee,status='p').update(status='pa')
    salaryemp.objects.filter(status='p').update(status='Generated')
    exist_emp = salaryemp.objects.filter(emid__in=Empoyee,status='pa')
    employees =addemployee.objects.filter(Employee_id=Employee_id)
    s=0
    for i in exist_emp:
        s+=float(i.payable)
    return render(request,'emppay.html',{'employees':employees,'s':s,'Empoyee':Empoyee})

def emp2(request,Employee_id):
    date=datetime.datetime.now().date()
    exist_emp = salaryemp.objects.filter(status='pa').update(status='Paid',date_of_payment=date)
    employees =addemployee.objects.filter(Employee_id=Employee_id)
    return render(request,'emppayfin.html',{'employees':employees})

def emp1(request,Employee_id):
    exist_emp = salaryemp.objects.filter(status='pa').update(status='Generated')
    employees =addemployee.objects.filter(Employee_id=Employee_id)
    return render(request,'emppayfin.html',{'employees':employees})



def addvendor(request,Employee_id):
    if request.method=='POST':
        id=len(vendor.objects.all())+1
        eid='VEN' +str(id)
      
        vendor_id = eid
        vendor_name =  request.POST['vendor_name']
        service_provided =  request.POST['service_provided']
        contact =  request.POST['contact']
        cost =  request.POST['cost']
        vendor_pan=  request.POST['vendor_pan']
        vendor_gst =  request.POST['vendor_gst']
        mode_of_pay =  request.POST['mode_of_pay']
        payment_duration =  request.POST['payment_duration']
        status =  request.POST['status']
        due_date =  request.POST['due_date']
        location = request.POST['location']
        email =  request.POST['email']
        month=str(due_date)
  
        month=month[:7]
        if cost==0:
            type_amt='Variable'
        else:
            type_amt='Fixed'
     
      

        
        if not vendor.objects.filter(email=email).exists():
            user=vendor.objects.create(cost=cost,contact=contact,paid_date=due_date,month=month,service_provided=service_provided,due_date=due_date,location=location,vendor_id=vendor_id,vendor_pan=vendor_pan,vendor_gst=vendor_gst,vendor_name=vendor_name,status=status,type_amt=type_amt,email=email,payment_duration=payment_duration,mode_of_pay=mode_of_pay)
            user.save()

        else:
            messages.info(request,'Vendor Exists')
        id=len(vendor.objects.all())+1
        eid='VEN' +str(id)
        
        employees =addemployee.objects.filter(Employee_id=Employee_id)
        print(Employee_id)
        return render(request,'addvendor.html',{'employees':employees,'eid':eid})
      
    
    else:
        id=len(vendor.objects.all())+1
        eid='VEN' +str(id)
        
        employees =addemployee.objects.filter(Employee_id=Employee_id)
        return render(request,'addvendor.html',{'employees':employees,'eid':eid})

def viewsvendor(request,id):
    v1=vendor.objects.filter(status='Active',pay_status='')
    v2=vendor.objects.filter(status='Active',pay_status='Paid').order_by("-paid_date")
    v3=vendor.objects.filter(status='Inactive')

    employees =addemployee.objects.filter(id=id)
    return render(request,'viewsvendor.html',{'employees':employees,'v1':v1,'v2':v2,'v3':v3})


    
def vendor_form(request,Employee_id,id=0):
    if request.method == "GET":
        employees =vendor.objects.filter(pk=id)
        print(employees)
        
     
        employees=addemployee.objects.filter(Employee_id=Employee_id)
        if id == 0:
            form = VendorForm()
        else:
            employee = vendor.objects.get(pk=id)
            form = VendorForm(instance=employee)
        return render(request, "vendor_form.html", {'form': form,'employees':employees})
    else:
        employee = vendor.objects.get(pk=id)
      
        employees=addemployee.objects.filter(Employee_id=Employee_id)
        for i in employees:
            ids=i.id
        form = VendorForm(request.POST,instance= employee)
       
        if form.is_valid():
            form.save()
            print('save')
            return redirect('viewsvendor',id=ids)
        else:
            return redirect('viewsvendor',id=id)




def taxfin(request,Employee_id):

    employees =addemployee.objects.filter(Employee_id=Employee_id)
    r=Receipt.objects.filter(balance_amt='Done')
    rl=[]
    for i in r:
        rl.append(i.receipt_id)

    tax=taxpayment.objects.filter(receipt_id__in=rl)
    t=0
    s=0
    c=0
    for i in tax:
        t+=float(i.tax)
        s+=float(i.sgst)
        c+=float(i.cgst)
    return render(request,'taxfin.html',{'employees':employees,'tax':tax,'ta':t,'sgst':s,'cgst':c})

def venpay(request,Employee_id,id):
    date=datetime.datetime.now().date()
    v=vendor.objects.filter(id=id)
    for i in v:
        vendorid=i.vendor_id
        cost=i.cost
        mode=i.mode_of_pay
    employees =addemployee.objects.filter(Employee_id=Employee_id)
    print(date)
    return render(request,'venpay.html',{'employees':employees,'date':date,'id':vendorid,'mode':mode,'cost':cost})



def venpay1(request,Employee_id):
    date=datetime.datetime.now().date()
    month=str(date)
  
    month=month[:7]
    
    if request.method=='POST':
        
        cost=request.POST['cost']
        bank_name=request.POST['bank_name']
        acc_no=request.POST['acc_no']
        vendor_id=request.POST['vendor_id']
        mode_of_pay=request.POST['mode_of_pay']
        vendor.objects.filter(vendor_id=vendor_id).update(paid_date=date,month=month,cost=cost,pay_status='Paid',bank_name=bank_name,acc_no=acc_no,mode_of_pay=mode_of_pay)
        employees =addemployee.objects.filter(Employee_id=Employee_id)
        v1=vendor.objects.filter(status='Active',pay_status='')
        v2=vendor.objects.filter(status='Active',pay_status='Paid').order_by("-paid_date")
        v3=vendor.objects.filter(status='Inactive')
        return render(request,'viewsvendor.html',{'employees':employees,'v1':v1,'v2':v2,'v3':v3})


def newpay(request,Employee_id):
    employees =addemployee.objects.filter(Employee_id=Employee_id)
    clients=Emp_Quot.objects.filter(status='Accepted')
    client_id=[]
    for i in clients:
        client_id.append(i.clientid)
    cl=Receipt.objects.filter(balance_amt='Done')
    ci=[]
    for i in cl:
        ci.append(i.client_id)
    c3=list(set(client_id)-set(ci))
    clients=Emp_Quot.objects.filter(clientid__in=c3)
    
    return render(request,'newpay.html',{'employees':employees,'clients':clients})

def addreceipt(request,Employee_id,clientid):
    clients=Emp_Quot.objects.filter(clientid=clientid)
    date=datetime.datetime.now().date()
    for i in clients:
        client_id=i.clientid
        client_name=i.client_name
        category=i.category
        total=i.total
    r=Receipt.objects.filter(client_id=client_id)
    amount_received=0
    for i in r:
        amount_received+=float(i.amount_received)
    balance_amount=float(total)-float(amount_received)
    employees =addemployee.objects.filter(Employee_id=Employee_id)
    rid=len(Receipt.objects.all())+1
    receipt_id='REC'+str(rid)
    return render(request,'addreceipt.html',{'employees':employees,'date':date,'total':total,'receipt_id':receipt_id,'client_id':client_id,'client_name':client_name,'category':category,'balance_amt':balance_amount})

def addreceipt1(request,Employee_id):
    client_id=request.POST['client_id']
    amount_received=request.POST['amount_received']
    next_duedate=request.POST['next_duedate']
    mode_of_pay=request.POST['mode_of_pay']
    cheque=request.POST['cheque']
    cheque_date=request.POST['cheque_date']
    bank_name=request.POST['bank_name']
    online_ref=request.POST['online_ref']
    date=datetime.datetime.now().date()
    c=client.objects.filter(clientid=client_id)
    clients=Emp_Quot.objects.filter(clientid=client_id)
    for i in clients:
        client_name=i.client_name
        category=i.category
        total=i.total
        second_amt=i.second_amt
        third_amt=i.third_amt
        balance=i.balance
    
    if(str(balance)!='Done' ):
        print('balance is')
        print(balance)
        if(balance=='0' or balance==''):
            Emp_Quot.objects.filter(clientid=client_id).update(second_payment_date=next_duedate,first_payment_date=date,first_amt=amount_received)

        elif (second_amt==0 or second_amt==''):
            Emp_Quot.objects.filter(clientid=client_id).update(third_payment_date=next_duedate, second_payment_date=date,second_amt=amount_received)
        else:
            Emp_Quot.objects.filter(clientid=client_id).update(third_payment_date=date,third_amt=amount_received)
    tax=float(total)-(float(total)/(1+0.18))
    sgst=float(total)-(float(total)/(1+0.18))
    cgst=float(total)-(float(total)/(1+0.18))
    sgst=round(sgst,3)
    cgst=round(cgst,3)
    tax=round(tax,3)
    rid=len(Receipt.objects.all())+1
    receipt_id='REC'+str(rid)
    Receipt.objects.create(client_id=client_id,tax=tax,receipt_id=receipt_id,totalvalue=total,cheque=cheque,category=category,next_duedate=next_duedate,mode_of_pay=mode_of_pay,client_name=client_name,cheque_date=cheque_date,online_ref=online_ref,bank_name=bank_name,amount_received=amount_received)
    
    r=Receipt.objects.filter(client_id=client_id)
    print(r)
    amount_received=0
    for i in r:
        
        amount_received+=float(i.amount_received)
    print(amount_received)
    balance_amt=float(total)-float(amount_received)
    print(total)
    print(balance_amt)
    if(float(balance_amt)==0):
        balance_amt='Done'
    Receipt.objects.filter(receipt_id=receipt_id).update(balance_amt=balance_amt)
    amount_paid=float(total)-float(balance_amt)
    Emp_Quot.objects.filter(clientid=client_id).update(balance=balance_amt,amount_paid=amount_paid)


    tax=sgst+cgst
    tax=round(tax,3)
    taxpayment.objects.create(client_id=client_id,receipt_id=receipt_id,sgst=sgst,cgst=cgst,tax=tax)
    clients=Emp_Quot.objects.filter(status='Accepted')
    employees =addemployee.objects.filter(Employee_id=Employee_id)
    return redirect('newpay',Employee_id=Employee_id)

def exreceipt(request,Employee_id):
    clients=Receipt.objects.all().order_by("-date")
    amt=0
    for i in clients:
        amt+=float(i.amount_received)
    employees =addemployee.objects.filter(Employee_id=Employee_id)
    return render(request,'exreceipt.html',{'employees':employees,'clients':clients,'amt':amt})
    
def receipt(request,receipt_id):
    print(receipt_id)
    r=Receipt.objects.filter(receipt_id=receipt_id)
    for i in r:
        id=i.client_id
        balance=i.balance_amt
        amount=i.amount_received
        online_ref=i.online_ref
        cheque=i.cheque
        date=i.date
    if cheque!='':
        max=True
    else:
        max=False
    amount=float(amount)/(1+0.18)
    amount=round(amount,3)
    if balance=='DONE':
        next=False
    else:
        next=True
    e=Emp_Quot.objects.filter(clientid=id)
    for i in e:
        qu=i.quotation_id
    return render(request,'receipt.html',{'date':date,'qu':qu,'r':r,'next':next,'amount':amount,'max':max})


    
def receiptdown(request,receipt_id):
    print(receipt_id)
    
    r=Receipt.objects.filter(receipt_id=receipt_id)
    for i in r:
        id=i.client_id
        balance=i.balance_amt
        amount=i.amount_received
        online_ref=i.online_ref
        cheque=i.cheque
        date=i.date
    if cheque!='':
        max=True
    else:
        max=False
    amount=float(amount)/(1+0.18)
    amount=round(amount,3)
    if balance=='DONE':
        next=False
    else:
        next=True
    e=Emp_Quot.objects.filter(clientid=id)
    for i in e:
        qu=i.quotation_id
    return render(request,'receiptdown.html',{'date':date,'qu':qu,'r':r,'next':next,'amount':amount,'max':max})


    
def recprint(request,receipt_id):
    print(receipt_id)
    
    r=Receipt.objects.filter(receipt_id=receipt_id)
    for i in r:
        id=i.client_id
        balance=i.balance_amt
        amount=i.amount_received
        online_ref=i.online_ref
        cheque=i.cheque
        date=i.date
    if cheque!='':
        max=True
    else:
        max=False
    amount=float(amount)/(1+0.18)
    amount=round(amount,3)
    if balance=='DONE':
        next=False
    else:
        next=True
    e=Emp_Quot.objects.filter(clientid=id)
    for i in e:
        qu=i.quotation_id
    return render(request,'recprint.html',{'date':date,'qu':qu,'r':r,'next':next,'amount':amount,'max':max})
    
