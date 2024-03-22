from django.shortcuts import render
from .models import Album, Event

# Create your views here.
def home(request):
    """
    View function to show the main home page. Takes you to home.html and makes you register or login.
    """
    return render(request, 'registration/home.html')

def login(request):
    return render(request, 'registration/login.html')

def register(request):
    return render(request, 'registration/register.html')