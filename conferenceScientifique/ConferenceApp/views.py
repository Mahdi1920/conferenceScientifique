from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from .models import Conference
from django.views.generic import ListView, DetailView

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to the Conference Management System</h1>")

def about(request):
    name="Conference App"
    return render(request, 'Conference/about.html', {'app_name': name})

def profile(request,username):
    return render(request, 'Conference/profile.html', {'username': username}) 

def conferenceList(request):
    list = Conference.objects.all().order_by('start_date')
    return render(request, 'Conference/conference_list.html', {'conferences': list})

class ConferenceListView(ListView):
    model = Conference
    context_object_name = 'conferences'
    template_name = 'Conference/conference_list.html'

class ConferenceDetailView(DetailView):
    model = Conference
    context_object_name = 'conference'
    template_name = 'Conference/conference_detail.html'