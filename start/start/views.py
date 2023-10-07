# views.py

from django.shortcuts import render, redirect
from .models import Event, IssueLog, Likes, Map, Profile, IssueLog
from .forms import EventForm, IssueLogForm
from django.shortcuts import render

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

def get_figure(request):
    issue_object = IssueLog.objects.all()
    mysolve_rows = issue_object.filter(Username=request.profile.user, usertype='SOLVER')
    citysolve_rows = issue_object.filter(City=request.profile.city, usertype='SOLVER')
    issue_percentage = mysolve_rows.count() / citysolve_rows.count()

    yourissue_solved = (issue_object.filter(Username=request.profile.user, usertype='POSTER')
                        .filter(usertype='SOLVER').values('issue_id').distinct())
    issue_post = issue_object.filter(Username=request.profile.user, usertype='POSTER')
    issue_posted = yourissue_solved / issue_post

    return render(request, 'profile.html', {'issue_percentage': issue_percentage,'issue_posted': issue_posted })
