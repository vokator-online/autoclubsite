from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('events/', views.EventListView.as_view(), name='events'),
    path('event/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
    path('cinema/', views.CinemaView.as_view(), name='cinema'),
    path('meetings/', views.MeetingsView.as_view(), name='meetings'),
    path('applications/', views.ApplicationsView.as_view(), name='applications'),
    path('merchandise/', views.MerchandiseView.as_view(), name='merchandise'),
    path('contact/', views.TicketCreateView.as_view(), name='contact'),
    path('tickets/', views.TicketList.as_view(), name='ticket_list'),
    path('ticket/<int:pk>/', views.TicketDetail.as_view(), name='ticket_detail'),
]
