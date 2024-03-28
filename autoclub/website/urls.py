from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('events/', views.EventsView.as_view(), name='events'),
    path('grand/', views.GrandView.as_view(), name='grand_meet_2023'),
    path('cinema/', views.CinemaView.as_view(), name='cinema'),
    path('meetings/', views.MeetingsView.as_view(), name='meetings'),
    path('applications/', views.ApplicationsView.as_view(), name='applications'),
    path('merchandise/', views.MerchandiseView.as_view(), name='merchandise'),
    path('contact/', views.TicketCreateView.as_view(), name='contact'),
    path('tickets/', views.TicketList.as_view(), name='ticket_list'),
    path('ticket/<int:pk>/', views.TicketDetail.as_view(), name='ticket_detail'),

]
