from tkinter import CASCADE
from unittest.mock import DEFAULT
from django.db import models

# Create your models here.
class Roles(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class EmployeeRegister(models.Model):
    Employee_ID = models.CharField(max_length=2)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=11)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name
    
    