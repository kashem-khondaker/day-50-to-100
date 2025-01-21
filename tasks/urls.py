from django.contrib import admin
from django.urls import path
from tasks.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/' , home),
    path('Manager-dashboard/' , Manager_dashboard),
    path('user-dashboard/', User_dashboard),
    path('test/' , test),
    path('task-list/' , task_list),
    path('add-task/', add_task, name='add-task'),
    path('add-project/', add_project, name='add-project'),
    path('add-employee/', add_employee, name='add-employee'),
]
