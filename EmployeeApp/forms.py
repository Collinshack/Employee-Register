from cProfile import label
from dataclasses import fields
from django import forms
from .models import EmployeeRegister 


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeRegister
        fields = ('first_name', 'last_name', 'Employee_ID', 'mobile', 'role')
     
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['role'].empty_label = "Select"