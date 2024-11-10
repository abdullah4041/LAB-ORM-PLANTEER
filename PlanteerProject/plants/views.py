from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse
from .models import Plant
from django.db import models
from django.utils import timezone

# Create your views here.


def plants_all(request: HttpRequest):
    plants = Plant.objects.all()  
    return render(request, "main/plants_all.html", {"plants": plants}) 

def add_new_page(request : HttpRequest):
    if request.method == "POST":
        new_plant = Plant(
        name=request.POST["name"],
        about=request.POST["about"],
        used_for=request.POST["used_for"],
        is_edible=request.POST.get("is_edible") == "on", 
        created_at=request.POST.get("created_at", timezone.now()),
         image=request.FILES.get("image"),
        category=request.POST["category"],
        )
        new_plant.save()
        return redirect('main:home_page')
    
    return render(request,"main/add_new.html")

def update_page(request : HttpRequest):
    return render(request,"main/update.html")

def plant_delete_view(request, plant_id):
    plant = Plant.objects.get(pk=plant_id)
    plant.delete()
    return redirect('main:home_page')  





def detail_page(request, plant_id):
   from django.shortcuts import render
from .models import Plant

def detail_page(request, plant_id):
    try:
        plant = Plant.objects.get(id=plant_id)
    except Plant.DoesNotExist:
        return render(request, 'main/home') 
    similar_plants = Plant.objects.filter(category=plant.category).exclude(id=plant.id)  # النباتات المشابهة

    return render(request, 'main/detail.html', {'plant': plant, 'plants': similar_plants})


def search_page(request : HttpRequest):
    return render(request,"main/search.html")
