from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.home, name='home'),
    path('user/', views.userPage, name='user_page'),
    path('account/', views.accountSettings, name='account_settings'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>/', views.customers, name='customer'),
    path('create_order/', views.createOrder, name='create_order'),
    path('create_customer/', views.createCustomer, name='create_customer'),
    path('update_order/<str:pk>/', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order')
]