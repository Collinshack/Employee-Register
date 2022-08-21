
from django.shortcuts import render, redirect
from .models import EmployeeRegister
from .forms import EmployeeForm
# Create your views here.


'''def new_employee(request, pk=0):
    form = EmployeeForm()
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    if request.method == 'POST':
        employee = EmployeeRegister.objects.get(id=pk)
        form = EmployeeForm(instance=employee)
        if pk == 0:
            form = EmployeeForm()
        else:
            employee = EmployeeRegister.objects.get(id=pk)
            form = EmployeeForm(request.POST, instance=employee)
            if form.is_valid():
                form.save()
                return redirect('employee_list')
    return render(request, 'employeeregister.html', {'form':form}) '''
    

def Employee_List(request):
    employee_lists = EmployeeRegister.objects.all()
    return render(request, 'employee_list.html', {'employee_lists': employee_lists})


def delete_employee(request, pk):
    employee = EmployeeRegister.objects.get(id=pk)
    employee.delete()
    return redirect('employee_list') 
    
    
def new_employee(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('employee_list')                
    return render(request, 'employeeregister.html', {'form':form})

def update_employee(request, pk):
    employee = EmployeeRegister.objects.get(id=pk)
    form = EmployeeForm(instance=employee)
    if request.method == 'POST':
        employee = EmployeeRegister.objects.get(id=pk)
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('employee_list')
    return render(request, 'editpage.html', {'form': form})