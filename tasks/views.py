from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is the home page...")

def Dashboard(request):
    return render(request , 'dashboard/dashboard.html')

def Manager_dashboard(request):
    return render(request, 'dashboard/manager-dashboard.html')

def User_dashboard(request):
    return render(request, 'dashboard/user_dash_board.html')