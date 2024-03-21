from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('events/', views.EventsView.as_view(), name='events'),
    path('cinema/', views.CinemaView.as_view(), name='cinema'),
    path('meetings/', views.MeetingsView.as_view(), name='meetings'),
    path('applications/', views.ApplicationsView.as_view(), name='applications'),
    path('merchandise/', views.MerchandiseView.as_view(), name='merchandise'),
    path('contact/', views.TicketCreateView.as_view(), name='contact'),
]
