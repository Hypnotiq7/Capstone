from django.shortcuts import render
from .models import Album, Event

# Create your views here.
def home(request):
    """
    View function to show the main home page. Takes you to home.html and makes you register or login.
    """
    return render(request, 'registration/home.html')

def login(request):
    """
    View function of the Login page. If you want to sign in with your username and password this is the page you looking for
    """
    return render(request, 'registration/login.html')

def register(request):
    """
    View function for anyone that needs to register. If you dont have username or password, you can sign up
    """
    return render(request, 'registration/register.html')