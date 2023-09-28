from django import forms
from .models import Emoplyee,Position

class Employeeform(forms.ModelForm):
    class Meta:
        model =Emoplyee
        fields =('FullName','emp_code','mobile','position')