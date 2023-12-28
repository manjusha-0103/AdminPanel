from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('save_user_to_firebase/', views.save_user_to_firebase, name='save_user_to_firebase'),
    path('', views.home, name='home'),
]