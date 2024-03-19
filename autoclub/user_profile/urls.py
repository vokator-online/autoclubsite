from django.urls import path
from . import views


urlpatterns = [
    path('registration/', views.UserRegisterView.as_view(), name='registration'),
    path('<int:pk>/profile/', views.ShowProfilePageView.as_view(), name='show_profile_page'),
    path('edit_profile/', views.UserEditView.as_view(), name='edit_profile'),   
    path('edit_profile_page/<int:pk>/', views.EditProfilePageView.as_view(), name='edit_profile_page'),
]
