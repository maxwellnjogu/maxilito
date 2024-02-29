from django.shortcuts import render

# Create your views here.
from models import Home
def home(request):
    return render(request, 'home.html')




return render(request, 'about.html',)


def about(request):


