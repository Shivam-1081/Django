from django.http import HttpResponse;
from django.shortcuts import render
from app.models import *
def home(request):
    return render (request , 'home.html')
def login(request):
    return render(request , 'login.html')
def base(request):
    return render(request , 'base.html')

# def register(request):
#     name = 'Shivam'
#     pno = '475837409934'
#     email = 'shivamsinghri45@gmail.com'
#     add= 'bhubaneshwar'
#     EO = Emp(ename= name, pno=pno,email=email)
#     return HttpResponse('Employeee registered Sucessfully')


def register(request):
    if request.method=='POST':
        name= request.POST.get('ename')
        pno = request.POST.get('pno')
        email= request.POST.get('email')
        address= request.POST.get('add')
        print(request.POST)
        EO = Students(name=name, pno=pno,email=email,gender=address)
        EO.save()
        return HttpResponse('Employeee registered Sucessfully')

    return render(request,'register.html')