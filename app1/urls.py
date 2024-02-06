from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views
from .views import reserve,download_pdf

urlpatterns = [
    path('test/', views.test , name='test'),
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
    path('reservationclient/<str:pk>/', views.reservationclient, name='reservationclient'),
    path('reserve/<str:pk>/', views.reserve, name='reserve'),
    path('hotels/', views.hotels , name='hotels'),
    path('addhotel/', views.addhotel , name='addhotel'),
    path('updatehotel/<str:pk>/', views.updatehotel, name='updatehotel'),
    path('deletehotel/<str:pk>/', views.deletehotel, name='deletehotel'),
    path('vols/', views.vols , name='vols'),
    path('addvol/', views.addvol , name='addvol'),
    path('updatevol/<str:pk>/', views.updatevol, name='updatevol'),
    path('deletevol/<str:pk>/', views.deletevol, name='deletevol'),
    path('admins/', views.admins , name='admins'),
    path('detailsvoyage/<str:pk>/', views.detailsvoyage, name='detailsvoyage'),
    path('categorievoyage/<str:pk>/', views.categorievoyage, name='categorievoyage'),

    # path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset_password"),
    # path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    # path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),

    path('clients/', views.clients , name='clients'),
    path('sendnotification/<str:pk>',views.sendnotification,name='sendnotification'),

    path('notifications/', views.notifications , name='notifications'),

    path('promotions/', views.promotions , name='promotions'),
    path('addpromotion/', views.addpromotion , name='addpromotion'),
    path('updatepromotion/<str:pk>/', views.updatepromotion, name='updatepromotion'),
    path('deletepromotion/<str:pk>/', views.deletepromotion, name='deletepromotion'),


    
    path('commentaire/', views.addcommentaire , name='commentaire'),

    path('download_pdf/<int:pk>/', download_pdf, name='download_pdf'),
]

