from django.shortcuts import render
from .models import Newfeed
def home(request):
    news = Newfeed.objects.all()
    return render(request,'newfeed/home.html',{'news':news})
