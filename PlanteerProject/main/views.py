from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from plants.models import Plant
# Create your views here.

def home_page(request):
    plants = Plant.objects.all()[:3]
    return render(request, 'main/home.html', {'plants': plants})

def contact_page(request : HttpRequest):
    return render(request,"main/contact.html")

def messages_page(request : HttpRequest):
    return render(request,"main/messages.html")

