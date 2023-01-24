from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('account/<slug:user_slug>/', views.profile, name='profile'),
    path('logout/', views.Logout, name='logout'),
]