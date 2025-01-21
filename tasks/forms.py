from django import forms 
from tasks.models import Task , Project , Employee

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['project' , 'title' , 'description' , 'due_date' , 'status' , 'priority']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name' , 'description']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name' , 'email' , ]
