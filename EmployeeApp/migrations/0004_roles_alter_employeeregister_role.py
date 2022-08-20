# Generated by Django 4.0.5 on 2022-08-19 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0003_rename_employee_id_employeeregister_employee_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='employeeregister',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmployeeApp.roles'),
        ),
    ]