from django.contrib import admin
from django.urls import path
from tasks.views import home ,Dashboard , Manager_dashboard , User_dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/' , home),
    path('Manager-dashboard/' , Manager_dashboard),
    path('user-dashboard/', User_dashboard)
]
