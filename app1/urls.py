from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name='home'),
    path('page2/', views.test2 , name='test2'),
    path('login/', views.loginPage , name='login'),
    path('register/', views.register , name='register'),
    path('registerAdmin/', views.registerAdmin , name='registerAdmin'),
    path('client/', views.ClientPage , name='client'),
    path('ClientSettings/', views.ClientSettings , name='ClientSettings'),
    path('AdminPage/', views.AdminPage , name='AdminPage'),
    path('logout/', views.logoutUser , name='logout'),
    path('voyages/', views.voyages , name='voyages'),
    path('addvoyage/', views.createvoyage , name='addvoyage'),
    path('updatevoyage/<str:pk>/', views.updatevoyage, name='updatevoyage'),
    path('deletevoyage/<str:pk>/', views.deletevoyage, name='deletevoyage'),
    path('categories/', views.categories , name='categories'),
    path('addcategorie/', views.addcategorie , name='addcategorie'),
    path('updatecategorie/<str:pk>/', views.updatecategorie, name='updatecategorie'),
    path('deletecategorie/<str:pk>/', views.deletecategorie, name='deletecategorie'),
]

