from django.urls import path
from . import views

urlpatterns = [
    # Home (public)
    path('', views.home, name='home'),

    # Car management
    path('cars/', views.car_list, name='car_list'),
    path('cars/create/', views.add_car, name='add_car'),
    path('cars/edit/<int:id>/', views.edit_car, name='edit_car'),
    path('cars/delete/<int:id>/', views.delete_car, name='delete_car'),
    path('cars/car/<int:car_id>/', views.car_detail, name='car_detail'),

    # Car booking
    path('register/', views.register_car, name='register_car'),
    path('registrations/', views.registrations_list, name='registrations_list'),

    # Authentication
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
