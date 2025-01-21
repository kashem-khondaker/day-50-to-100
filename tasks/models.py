from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)
    joined_at = models.DateTimeField(auto_now_add=True)

    # projects for revers access

class Project(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    employees = models.ManyToManyField(Employee , related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)

    # Tasks for reverse join


class Task(models.Model):
    
    # for status Choice : 
    pending = 'Pending'
    completed = 'Completed'
    status_choice = [
        (pending , 'Pending'),
        (completed , 'Completed')
    ]

    # for Priority choice : 
    High = 'High'
    Medium = 'Medium'
    Low = 'Low'
    Priority_choice = [
        (High , 'High'),
        (Medium , 'Medium'),
        (Low , 'Low')
    ]

    project = models.ForeignKey(Project , on_delete=models.CASCADE , related_name='Tasks', default=1)

    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    status = models.TextField(max_length=20 , choices=status_choice , default=pending)
    priority = models.TextField(max_length=20 , choices=Priority_choice , default=Low)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


