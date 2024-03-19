from django.urls import path
# from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import PasswordChangeDoneView
from . import views


urlpatterns = [
    path('registration/', views.UserRegisterView.as_view(), name='registration'),
    path('<int:pk>/profile/', views.ShowProfilePageView.as_view(), name='show_profile_page'),
    path('edit_profile/', views.UserEditView.as_view(), name='edit_profile'),   
    path('edit_profile_page/<int:pk>/', views.EditProfilePageView.as_view(), name='edit_profile_page'),
    # path('password_change/',views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'), 
    # path('change_password/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
]
