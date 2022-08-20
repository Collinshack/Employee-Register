from tkinter import E
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import EmployeeRegister
from .forms import EmployeeForm
# Create your views here.


def new_employee(request, pk=0):
    if request.method == 'GET':
        form = EmployeeForm()
        if pk ==0:
            form = EmployeeForm()
        else:
            employee = EmployeeRegister.objects.get(id=pk)
            form = EmployeeForm(instance=employee)  
        return render(request, 'employeeregister.html', {'form': form})             
    else:
        if pk == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = EmployeeRegister.objects.get(id=pk)
            form = EmployeeForm(request.POST, instance=employee)           
        if form.is_valid():
            form.save()
        return redirect('employee_list')
       


def Employee_List(request):
    employee_lists = EmployeeRegister.objects.all()
    return render(request, 'employee_list.html', {'employee_lists': employee_lists})


def delete_employee(request, pk):
    employee = EmployeeRegister.objects.get(id=pk)
    employee.delete()
    return redirect('employee_list')