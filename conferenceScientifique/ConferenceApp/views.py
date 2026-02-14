from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

from SessionApp.models import Session
from .forms import ConferenceForm
from .models import Conference
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import DeleteView, UpdateView

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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        conference = self.get_object()
        context['sessions'] =Session.objects.filter(conference=conference)
        return context


class ConferenceDeleteView(DeleteView):
    model = Conference
    context_object_name = 'conference'
    template_name = 'Conference/conference_delete.html'
    success_url = reverse_lazy('conference_lv')

class ConferenceCreateView(CreateView):
    model = Conference
    form_class = ConferenceForm
    template_name = 'Conference/conference_form.html'
    success_url = reverse_lazy('conference_lv')

class ConferenceUpdateView(UpdateView):
    model = Conference
    form_class = ConferenceForm
    template_name = 'Conference/conference_form.html'
    success_url = reverse_lazy('conference_lv')