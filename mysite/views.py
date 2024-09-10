from django.shortcuts import render
from django.contrib.auth import logout as django_logout
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from decouple import config
import json

# Create your views here.

def index(request):
    return render(request, 'index.html')

def cart(request):
    return render(request, 'cart.html')  # Ensure this view exists

def tracer(request):
    return render(request, 'tracer.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')


def logout(request):
    django_logout(request)

    domain = config('APP_DOMAIN')
    client_id = config('APP_CLIENT_ID')
    return_to = 'http://127.0.0.1:8000/'

    return HttpResponseRedirect(f"https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}")

def profile(request):
    user = request.user

    # Assuming 'auth0' is the provider's name as a string
    auth0_user = user.social_auth.get(provider='auth0')

    user_data = {
        'user_id': auth0_user.uid,
        'name': user.first_name,
        'picture': auth0_user.extra_data.get('picture')
    }

    context = {
        'user_data': json.dumps(user_data, indent=4),
        'auth0_user': auth0_user
    }

    return render(request, 'profile.html', context)
