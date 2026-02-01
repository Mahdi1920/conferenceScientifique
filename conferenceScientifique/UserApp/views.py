from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from django.views.generic import ListView, DetailView

# Create your views here.

def home(request):
    return HttpResponse("<h1>Welcome to the User Management System</h1>")

def about(request):
    name="User App"
    return render(request, 'User/about.html', {'app_name': name})

def profile(request,username):
    return render(request, 'User/profile.html', {'username': username}) 
class UserListView(ListView):
    model=User
    context_object_name='users'  
    template_name='User/user_list.html'

class UserDetailView(DetailView):
    model=User
    context_object_name='user'  
    template_name='User/user_detail.html'