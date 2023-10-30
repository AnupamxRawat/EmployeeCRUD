from django import forms
from .models import Emoplyee,Position

class Employeeform(forms.ModelForm):
    class Meta:
        model =Emoplyee
        fields =('FullName','emp_code','mobile','position')

    ''' def __init__(self,*args,**kwargs):
        super(Employeeform,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label="Select"    

        #this is used to change label of  field in form page , as we have directly used form
        If we had made it , then  we should edit in the form view function
    '''