from django.shortcuts import render
from .forms import Employeeform
# Create your views here.

def emp_list(request):
    return render(request,"emp_list.html")

def emp_form(request):
    form=Employeeform()
    return render(request,'emp_form.html',{'form':form})


