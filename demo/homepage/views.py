from django.shortcuts import render
from . models import Employee
# Create your views here.

def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'aboutus.html')

def admin_login(request):
    return render(request,'adminlogin.html')

def contact(request):
    return render(request,'contactus.html')

def admincheck(request):

    username = request.POST['txtUsername']
    password = request.POST['txtPassword']

    if(username=='admin' and password=='super'):
        return render(request,'admindashboard.html')
    else:
        return render(request,'error.html')


def error(request):
    return render(request,'error.html')

def addemployee(request):
    return render(request,'adminAddEmployee.html')

def regsuccess(request):
    if request.method =='POST':

     i = request.POST['txtEmpId']
    n = request.POST['txtName']
    e = request.POST['txtEmail']
    m = request.POST['txtMobile']
    d = request.POST['txtDesignation']
    s = request.POST['txtSalary']
    x = Employee(request.POST)

    x.empid = i
    x.empname = n
    x.empemail = e
    x.empmobile  = m
    x.empdesignation = d
    x.empsalary = s

    x.save()

    return render(request,'adminRegSuccess.html')

def showemployee(request):

    x = Employee.objects.all()

    return render(request,'adminShowEmployee.html',{'emplist' : x})

def showsinglrecord(request,empid):

    x = Employee.objects.get(empid = empid)

    return render(request,'adminSingleRecord.html',{'emplist' : x})

def updaterecord(request,empid):
    if request.method =='POST':

     i = request.POST['txtEmpId']
    n = request.POST['txtName']
    e = request.POST['txtEmail']
    m = request.POST['txtMobile']
    d = request.POST['txtDesignation']
    s = request.POST['txtSalary']

    x = Employee.objects.get(empid = empid)

    x.empid = i
    x.empname = n
    x.empemail = e
    x.empmobile  = m
    x.empdesignation = d
    x.empsalary = s

    x.save()
    return render(request,'adminUpdateSuccess.html')

def deleterecord(request,empid):

    if request.method == 'POST':
        x = Employee.objects.get(empid=empid)
    x.delete()
    return render(request, 'adminDeleteRecord.html')

def logout(request):
    return render(request,'logout.html')










