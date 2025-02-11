# Generated by Django 4.1 on 2022-09-03 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0022_attendance_created_at_attendance_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='leave',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='leave',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='role',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='role',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
