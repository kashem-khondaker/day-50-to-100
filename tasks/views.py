from django.shortcuts import render , redirect
from django.http import HttpResponse
from tasks.models import Task , Project , Employee
from tasks.forms import TaskForm , ProjectForm , EmployeeForm


# Create your views here.
def home(request):
    return HttpResponse("This is the home page...")

def Dashboard(request):
    return render(request , 'dashboard/dashboard.html')

def Manager_dashboard(request):
    return render(request, 'dashboard/manager-dashboard.html')

def User_dashboard(request):
    return render(request, 'dashboard/user_dash_board.html')

def test(request):

    fruit_color = {
        'Apple': ['Red', 'Green'],
        'Banana': ['Yellow'],
        'Cherry': ['Red', 'Dark Red']
    }
    context={
        'fruits':fruit_color
    }
    return render(request , 'test.html' , context)


def task_list(request):
    tasks = Task.objects.all()
    context = {
        'tasks':tasks
    }
    return render(request , 'dashboard/task_list.html' , context)

# add task ----
def add_task(request):
    form = TaskForm(request.POST)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('task-list')
        else:
            return HttpResponse("Form is not valid or something went wrong . try again later...")
    context = {
        'form' : form,
    }
    return render(request , 'tasks/add_task.html' , context)

# add Project ----
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('home')  # Redirect to the home page or a project list view
    else:
        form = ProjectForm()
    return render(request, 'tasks/add_project.html', {'form': form})


# Add Employee
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page or employee list view
    else:
        form = EmployeeForm()
    return render(request, 'tasks/add_employee.html', {'form': form})