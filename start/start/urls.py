# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.event_list, name='event_list'),
    path('events/create/', views.create_event, name='create_event'),
    path('issues/', views.issue_list, name='issue_list'),
    path('issues/create/', views.create_issue, name='create_issue'),
]
