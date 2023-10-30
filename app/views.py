from django.shortcuts import render,redirect
from .forms import Employeeform
from .models import Emoplyee
# Create your views here.

def emp_list(request):
    con={'emp_list':Emoplyee.objects.all()}
    return render(request,"emp_list.html",con)

def emp_form(request,id=0):
    if request.method =="GET":
    
      if(id==0):
       form=Employeeform()
      else:
         employee=Emoplyee.objects.get(pk=id)
         form=Employeeform(instance=employee)
      return render(request,'emp_form.html',{'form':form})
    
    else:
       if id==0:
        form=Employeeform(request.POST)
       else:
         employee=Emoplyee.objects.get(pk=id)
         form=Employeeform(request.POST,instance=employee)
       if form.is_valid():
        form.save()
       return redirect('/list/') 

def delete(request,id):
  employee=Emoplyee.objects.get(pk=id)
  employee.delete()
  return redirect('/list')

