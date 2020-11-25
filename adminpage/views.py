from django.shortcuts import render,redirect
from django.contrib.auth import logout,login
from django.contrib import messages
from django.contrib.auth.models import auth,User
from hr.models import leave,salaryemp
from ERP.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from . forms import EmployeeForm,ServiceForm,announce,ImageForm
from . models import addemployee,addservices,discount,announcement
from finance.models import vendor,Receipt,taxpayment
from marketing.models import Emp_Quot, client
from finance.forms import VendorForm
import datetime



def exreceiptad(request):
    clients=Receipt.objects.all().order_by("-date")
    amt=0
    for i in clients:
        amt+=float(i.amount_received)

    return render(request,'exreceiptad.html',{'clients':clients,'amt':amt})

def logout(request):
    auth.logout(request)
    return redirect('adlogin')
# Create your views here.

def new_emp(request):
    context=addemployee.objects.filter(msg='') | addemployee.objects.filter(msg=0)
    print(context)

    return render(request, "new_emp.html", {'context':context})


def exist_emp(request):
    context = {'exist_emp': addemployee.objects.all()}
    return render(request, "exist_emp.html", context)


def adminportal(request):

    return render(request,'adminportal.html')

def addemp(request):
    if(request.method=='POST'):
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
        return redirect('addemp')

    else:
        
        id=len(addemployee.objects.all())+1
        eid='EM' +str(id)
    
        return render(request,'addemp.html',{'empid':eid})

    
def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = addemployee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_form.html", {'form': form})
    else:
        employee = addemployee.objects.get(pk=id)
        form = EmployeeForm(request.POST,instance= employee)
        print(form)
        if form.is_valid():
            form.save()
            print('save')
            return redirect('exist_emp')
        else:
            return redirect('exist_emp')

		


def view_services(request):
    context = {'services': addservices.objects.all()}
    return render(request, "view_services.html", context)


def new_services(request, id=0):
    if request.method == "GET":
        sid=len(addservices.objects.all())+1
        sid='SER' +str(sid)
   
        if id == 0:
            form = ServiceForm()
        else:
            employee = addservices.objects.get(pk=id)
            form = ServiceForm(instance=employee)
        return render(request, "new_services.html", {'form': form,'serid' :sid})
    else:
        rid=len(addservices.objects.all())+1
        sid='SER' +str(rid)
        if id == 0:
            form = ServiceForm(request.POST)

        else:
            employee = addservices.objects.get(pk=id)
            form = ServiceForm(request.POST,instance= employee)

        if form.is_valid():
            form.save()

        context=addservices.objects.last()

        addservices.objects.filter(id=context.pk).update(service_id=sid)
        
        return redirect('view_services')


def services_delete(request,id):
    employee = addservices.objects.get(pk=id)
    employee.delete()
    return redirect('view_services')

       
  
def discounts(request):
    if(request.method=='POST'):
        dis_per =  request.POST['dis_per']
        from_date =  request.POST['from_date']
        to_date =  request.POST['to_date']
        #sid=len(addservices.objects.all())+1
        #sid='SER' +str(sid)
        service_id=request.POST['service_id']

        user=discount.objects.create(dis_per=dis_per,from_date=from_date,to_date=to_date,service_id=service_id)
        user.save()

        return redirect('view_services')

    else:

        return render(request,'view_services.html')   

        

def view_announce(request):
    context = {'announces': announcement.objects.all().order_by('-date')[:5]}
    return render(request, "view_announce.html", context)


def new_announce(request, id=0):
    if request.method == "GET":
   
        if id == 0:
            form = announce()
        else:
            employee = announcement.objects.get(pk=id)
            form = announce(instance=employee)
        return render(request, "new_announce.html", {'form': form})
    else:
        if id == 0:
            form = announce(request.POST)

        else:
            employee = announcement.objects.get(pk=id)
            form = announce(request.POST,instance= employee)

        if form.is_valid():
            form.save()
        context=announcement.objects.last()

        announcement.objects.filter(id=context.pk).update(announce_by='Admin')
        subject = 'New Announcement from Techvolt'
        s=announcement.objects.filter(id=context.pk)
        from_email='techvolt123@gmail.com'
        for i in s:
            message1=i.message
        
        message = "Welcome, "+'\n\n'+message1+'\n'+'\n'+"Thanks and Regards,"+'\n'+"Admin."
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
        

        return redirect('view_announce')

def upload_photo(request,Employee_id):

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            m = addemployee.objects.get(Employee_id=Employee_id)
            m.image = form.cleaned_data['image']
            m.save()
            return redirect('view_profile',Employee_id=Employee_id)
        else:
            print("not valid")
    return redirect('view_profile',Employee_id=Employee_id)         

def upload_photo1(request,Employee_id):

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            m = addemployee.objects.get(Employee_id=Employee_id)
            m.image = form.cleaned_data['image']
            m.save()
            return redirect('view_mar',Employee_id=Employee_id)
        else:
            print("not valid")
    return redirect('view_mar',Employee_id=Employee_id) 

def upload_photo2(request,Employee_id):

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            m = addemployee.objects.get(Employee_id=Employee_id)
            m.image = form.cleaned_data['image']
            m.save()
            return redirect('view_fin',Employee_id=Employee_id)
        else:
            print("not valid")
    return redirect('view_fin',Employee_id=Employee_id) 

def upload_photo3(request,Employee_id):

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            m = addemployee.objects.get(Employee_id=Employee_id)
            m.image = form.cleaned_data['image']
            m.save()
            return redirect('view_tech',Employee_id=Employee_id)
        else:
            print("not valid")
    return redirect('view_tech',Employee_id=Employee_id) 

def change_pass(request,Employee_id):
    new_pass=request.POST['new_pass']
    confirm_pass=request.POST['con_pass']
    if(new_pass==confirm_pass):
        addemployee.objects.filter(Employee_id=Employee_id).update(password=new_pass)
        subject = 'Welcome to Techvolt'
        s=addemployee.objects.filter(Employee_id=Employee_id)
        for i in s:
            full=i.full_name
            password=i.password
            pemail=i.pemail

        message = 'Welcome '+full+","+'\n\n'+'Your Password is changed successfully.'+'\n'+"Your Password is "+password+'\n'+'\n'+"Thanks and Regards,"+'\n'+"Admin."
        recepient = str(pemail)
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        messages.info(request,'Password changed Successfully')
        return redirect('logout',Employee_id=Employee_id)
    else:
        messages.info(request,'Password not matched!')
        return redirect('view_profile',Employee_id=Employee_id)

def change_pass1(request,Employee_id):
    new_pass=request.POST['new_pass']
    confirm_pass=request.POST['con_pass']
    if(new_pass==confirm_pass):
        addemployee.objects.filter(Employee_id=Employee_id).update(password=new_pass)
        subject = 'Welcome to Techvolt'
        s=addemployee.objects.filter(Employee_id=Employee_id)
        for i in s:
            full=i.full_name
            password=i.password
            pemail=i.pemail

        message = 'Welcome '+full+","+'\n\n'+'Your Password is changed successfully.'+'\n'+"Your Password is "+password+'\n'+'\n'+"Thanks and Regards,"+'\n'+"Admin."
        recepient = str(pemail)
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        messages.info(request,'Password changed Successfully')
        return redirect('logout',Employee_id=Employee_id)
    else:
        messages.info(request,'Password not matched!')
        return redirect('view_mar',Employee_id=Employee_id)

def change_pass2(request,Employee_id):
    new_pass=request.POST['new_pass']
    confirm_pass=request.POST['con_pass']
    if(new_pass==confirm_pass):
        addemployee.objects.filter(Employee_id=Employee_id).update(password=new_pass)
        subject = 'Welcome to Techvolt'
        s=addemployee.objects.filter(Employee_id=Employee_id)
        for i in s:
            full=i.full_name
            password=i.password
            pemail=i.pemail

        message = 'Welcome '+full+","+'\n\n'+'Your Password is changed successfully.'+'\n'+"Your Password is "+password+'\n'+'\n'+"Thanks and Regards,"+'\n'+"Admin."
        recepient = str(pemail)
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        messages.info(request,'Password changed Successfully')
        return redirect('logout',Employee_id=Employee_id)
    else:
        messages.info(request,'Password not matched!')
        return redirect('view_fin',Employee_id=Employee_id)

def change_pass3(request,Employee_id):
    new_pass=request.POST['new_pass']
    confirm_pass=request.POST['con_pass']
    if(new_pass==confirm_pass):
        addemployee.objects.filter(Employee_id=Employee_id).update(password=new_pass)
        subject = 'Welcome to Techvolt'
        s=addemployee.objects.filter(Employee_id=Employee_id)
        for i in s:
            full=i.full_name
            password=i.password
            pemail=i.pemail

        message = 'Welcome '+full+","+'\n\n'+'Your Password is changed successfully.'+'\n'+"Your Password is "+password+'\n'+'\n'+"Thanks and Regards,"+'\n'+"Admin."
        recepient = str(pemail)
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        messages.info(request,'Password changed Successfully')
        return redirect('logout',Employee_id=Employee_id)
    else:
        messages.info(request,'Password not matched!')
        return redirect('view_tech',Employee_id=Employee_id)


def view_approve(request):

     
        leaves=leave.objects.filter(status='Accepted')
        leavesm=leave.objects.filter(status='Rejected')
        return render(request, "view_approve.html", {'leaves':leaves,'leavesm':leavesm})


def new_approve(request):
        leaves=leave.objects.filter(status='Pending',branch='Human Resource')
        return render(request, "new_approve.html", {'leaves':leaves})

def approve(request,id):
        leave.objects.filter(id=id).update(status='Accepted')
        return redirect("new_approve")

def reject(request,id):
        leave.objects.filter(id=id).update(status='Rejected')
        return redirect("new_approve")

def submit(request,pemail):
    
    subject = 'Welcome to Techvolt'
    s=addemployee.objects.filter(pemail=pemail)
    for i in s:
        full=i.full_name
        password=i.password
        user=i.username

    message = 'Welcome '+full+","+'\n\n'+'Your Username is '+user+'\n'+"Your Password is "+password+'\n'+'\n'+"Thanks and Regards,"+'\n'+"Admin."
    recepient = str(pemail)
    send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
    print('email sent')
    addemployee.objects.filter(pemail=pemail).update(msg='Sent')
    return redirect("new_emp")

def adpay(request):
    if (request.method=='POST'):
        month=request.POST['month']
        salar=salaryemp.objects.filter(month=month)
        sal=salaryemp.objects.filter(month=month,status='Generated')
        salary=salaryemp.objects.filter(month=month,status='Paid')
        total=0
        balance=0
        amount=0
        for i in sal:
            balance+=float(i.payable)
        for i in salary:
            amount+=float(i.payable)
        for i in salar:
            total+=float(i.payable)
        return render(request,'pastpay1.html',{'sal':sal,'salary':salary,'total':total,'amount':amount,'balance':balance})



    else:
        return render(request,'adpay.html')

def taxad(request):
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
    return render(request,'taxad.html' ,{'tax':tax,'ta':t,'sgst':s,'cgst':c})


def vpay(request):
    if (request.method=='POST'):
        month=request.POST['month']
        salar=vendor.objects.filter(month=month,status='Active')
        sal=vendor.objects.filter(month=month,status='Active',pay_status='')
        salary=vendor.objects.filter(month=month,pay_status='Paid')
        total=0
        balance=0
        amount=0
        for i in sal:
            balance+=float(i.cost)
        for i in salary:
            amount+=float(i.cost)
        for i in salar:
            total+=float(i.cost)
        return render(request,'vpay1.html',{'sal':sal,'salary':salary,'total':total,'amount':amount,'balance':balance})



    else:
        return render(request,'vpay.html')

def viewvendor(request):
    v1=vendor.objects.filter(status='Active').order_by('-month')
    v3=vendor.objects.filter(status='Inactive').order_by('-month')
    return render(request,'viewvendor.html',{'v1':v1,'v3':v3})


    
def ven_form(request,id=0):
    if request.method == "GET":
        employees =vendor.objects.filter(pk=id)
        print(employees)
        if id == 0:
            form = VendorForm()
        else:
            employee = vendor.objects.get(pk=id)
            form = VendorForm(instance=employee)
        return render(request, "ven_form.html", {'form': form,'employees':employees})
    else:
        employee = vendor.objects.get(pk=id)
      
        form = VendorForm(request.POST,instance= employee)
       
        if form.is_valid():
            form.save()
            print('save')
            return redirect('viewvendor')
        else:
            return redirect('viewvendor')

def proclient(request):
    client=Emp_Quot.objects.filter(project_leader='0',status='Accepted') | Emp_Quot.objects.filter( project_leader='',status='Accepted')
    print(client)
    s=[]
    for i in client:
        am=i.amount_paid
        if(float(am)*2>=float(i.total)):
            Emp_Quot.objects.filter(clientid=i.clientid).update(work=True)
    r=addemployee.objects.filter(dept='Technical')
      
   
    return render(request,'proclient.html',{'client':client,'r':r})

def proall(request):
    clientid=request.POST['clientid']
    project_end_date=request.POST['project_deadline']
    project_=request.POST['project_leader']
    date=datetime.datetime.now().date()
    status='Ongoing'
    print(clientid)
    Emp_Quot.objects.filter(clientid=clientid).update(project_end_date=project_end_date,project_start_date=date,project_status=status,project_leader=project_)

    client=Emp_Quot.objects.filter(project_leader='0',status='Accepted') | Emp_Quot.objects.filter( project_leader='',status='Accepted')
    print(client)
    s=[]
    for i in client:
        am=i.amount_paid
        if(float(am)*2>=float(i.total)):
            Emp_Quot.objects.filter(clientid=i.clientid).update(work=True)
    r=addemployee.objects.filter(dept='Technical')
      
   
    return render(request,'proclient.html',{'client':client,'r':r})


def exclient(request):
    client=Emp_Quot.objects.filter(project_status='Ongoing') | Emp_Quot.objects.filter( project_status='Completed')
    return render(request,'exclient.html',{'client':client})


def clienthist(request):
    clients=Emp_Quot.objects.filter(project_status='Ongoing') | Emp_Quot.objects.filter( project_status='Completed')
  
    openclients= client.objects.filter(status='Opened')
    closeclients= client.objects.filter(status='Closed')

    return render(request,'clienthist.html',{'clients':clients,'openclients':openclients,'closeclients':closeclients})


def clientdata(request,clientid):
    clients= client.objects.filter(clientid=clientid)
    return render(request,'clientdata.html',{'clients':clients})
    
def clientda(request,clientid):
    clients= client.objects.filter(clientid=clientid)
    return render(request,'clientda.html',{'clients':clients})