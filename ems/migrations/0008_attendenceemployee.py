# Generated by Django 4.1 on 2022-08-27 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0007_employee_emergency_mobile_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendenceEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intime', models.TimeField()),
                ('outtime', models.TimeField()),
                ('present', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ems.employee')),
            ],
        ),
    ]