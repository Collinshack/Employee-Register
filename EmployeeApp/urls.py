from django.urls import path
from . import views 
urlpatterns = [
    path('', views.new_employee, name='employee_register'),
    path('<int:pk>', views.new_employee, name='employee_update'),
    path('employee_list', views.Employee_List, name='employee_list'),
    path('delete_employee/<str:pk>/', views.delete_employee, name='delete_employee'),
]
