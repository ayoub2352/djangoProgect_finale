from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name='home'),
    path('page2/', views.test2 , name='test2'),
    path('login/', views.loginPage , name='login'),
    path('register/', views.register , name='register'),
    path('client/', views.ClientPage , name='client'),
    path('logout/', views.logoutUser , name='logout'),
]