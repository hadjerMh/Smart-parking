"""SmartParking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Inscription.views import inscription_view, loginView, logoutView, userpage, bienvenue
from parking.views import PlacesStatesUser, MakeReservation, reclamations, success_qrcode
from django.contrib.auth import views as auth_views
from parking.api.views import places_ipa, reservation_api, reservation_update_api, places_update, reservation_detail_api, reclamation_api
from admin_auth.views import admin_inscription, login_user, admin_home_view, admin_parking_create, logoutUser, admin_profil_update, admin_parking_update, parking_delete, dashbord, parking_details
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',bienvenue, name='bienvenue'),
    path('Inscription/', inscription_view, name='Inscription'),
    path('Reservation/', MakeReservation, name='Reservation'),
    path('Connexion/', loginView, name='Connexion' ),
    path('Deconnexion/', logoutView, name='Deconnexion'),
    path('Accueil/', PlacesStatesUser, name='home'),
    path('Reclamation/', reclamations, name='reclamations'),
    path('Profil/', userpage, name='profil'),
    path('reservation_success/', success_qrcode, name='reservation_success'),

    path('api_places/<str:parking>', places_ipa, name='api_places'),
    path('api_reservation/', reservation_api, name='api_reservation'),
    path('Reservation/update_reservation/<str:pk>/', reservation_update_api, name='api_reservation_update'),
    path('Reservation/detail_reservation/<str:pk>/',reservation_detail_api, name='reservation_detail_api'),
    path('Reservation/update_places/<str:pk1>/', places_update, name='places_update'),
    path('reclamation_api/<str:id>/', reclamation_api, name='reclamation_api'),

    
    path('administrateur/', admin_home_view, name="administrateur_homes"),
    path('administrateur_creation_parking/', admin_parking_create, name="administrateur_creation_parking"),
    path('Inscription_admin/', admin_inscription, name='Inscription_admin'),
    path('Connexion_admin/', login_user, name='Connexion_admin'),
    path('Deconnexion_admin/', logoutUser, name='Deconnexion_admin'),
    path('Profil_admin/',admin_profil_update , name='profil_admin'),
    path('Parking_update/<str:id>/', admin_parking_update, name='Parking_update'),
    path('Parking_delete/', parking_delete, name='Parking_delete'),
    path('Parking_detail/<str:id>/', parking_details, name='Parking_detail'),
    path('Dashbord/', dashbord, name='Dashbord'),

   
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'), name='password_reset_complete'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)