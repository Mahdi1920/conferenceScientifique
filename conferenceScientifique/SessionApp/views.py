from django.http import HttpResponse
from django.shortcuts import render
from .models import Session
from django.views.generic import ListView, DetailView

# Create your views here.

def home(request):
    return HttpResponse("<h1>Welcome to the Session Management System</h1>")

def about(request):
    name="Session App"
    return render(request, 'Session/about.html', {'app_name': name})

def profile(request,username):
    return render(request, 'Session/profile.html', {'username': username}) 
class SessionListView(ListView):
    model=Session
    context_object_name='sessions'  
    template_name='Session/session_list.html'

class SessionDetailView(DetailView):
    model=Session
    context_object_name='session'  
    template_name='Session/session_detail.html'