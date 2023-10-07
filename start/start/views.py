# views.py

from django.shortcuts import render, redirect
from .models import Event, IssueLog, Likes, Map, Profile
from .forms import EventForm, IssueLogForm

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})

def issue_list(request):
    issues = IssueLog.objects.all()
    return render(request, 'issue_list.html', {'issues': issues})

def create_issue(request):
    if request.method == 'POST':
        form = IssueLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('issue_list')
    else:
        form = IssueLogForm()
    return render(request, 'create_issue.html', {'form': form})
