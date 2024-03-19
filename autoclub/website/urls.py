from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('events.html', views.events, name="events"),
    path('cinema.html', views.cinema, name="cinema"),
    path('meetings.html', views.meetings, name="meetings"),
    path('applications.html', views.applications, name="applications"),
    path('merchandise.html', views.merchandise, name="merchandise"),
    path('contact.html', views.contact, name="contact"),
]
