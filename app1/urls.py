from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name='home'),
    path('page2/', views.test2 , name='test2'),
]