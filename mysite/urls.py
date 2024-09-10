from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('cart/', views.cart, name='cart'),  # Ensure this is defined
    path('wishlist/', views.wishlist, name='wishlist'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('tracer/', views.tracer, name='tracer'),
    path('', include('social_django.urls')),  # Includes the social auth URLs

]