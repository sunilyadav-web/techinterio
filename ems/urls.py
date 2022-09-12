from django.urls import path
from .views import *
app_name='ems'
urlpatterns=[
    path('',dashboard,name='ems'),
    path('create-department/',createDepartment,name='create-department'),
    path('view-departments/',viewDepartment,name='view-department'),
    path('delete-department/<pk>/',deleteDepartment,name='delete-department'),
    path('create-role/',createRole,name='create-role'),
    path('view-roles/',viewRole,name='view-role'),
    path('delete-role/<pk>/',deleteRole,name='delete-role'),
    path('add-personal-info/',addEmployee,name='add-employee'),
    path('employee-view/',viewEmployee,name='employee-view'),
    path('employee-detail/<empid>/',employeeDetail,name='employee-detail'),
    path('employee-delete/<empid>/',deleteEmployee,name='employee-delete'),
    path('attendance/',attendance,name='attendance'),
    path('attendance-edit/',editAttendance,name='edit-attendance'),
    path('attendance-delete/<pk>/',deleteAttendance,name='attendance-delete'),
    path('leave-create/',createLeave,name='leave-create'),
    path('leave-delete/<pk>/',deleteLeave,name='leave-delete'),
    path('leaves/',dashboardLeaves,name='dashboard-leaves'),
    path('profile/',profile,name='profile'),
    path('profile-edit/',editProfile,name='profile-edit'),
    path('change-password/',changePassword,name='change-password'),
    path('all-leaves/',allLeaves,name='all-leaves'),
    path('all-attendance/',allAttendances,name='all-attendance'),
    path('create-event/',createEvent,name='create-event'),
    path('view-events/',viewEvents,name='view-events'),
    path('delete-event/<id>/',deleteEvent,name='delete-event'),
    path('event/<id>/',event,name='event'),
    path('create-payroll',createPayRoll,name='create-payroll'),
    
]