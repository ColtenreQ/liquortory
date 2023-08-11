from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Liquor

from .forms import *

# Function for creating the home page.
def home(request):
    hometemplate_name = "home.html"

    liquorListAlmostOut = Liquor.objects.filter(numberOfBottles__lt=3)

    return render(request, hometemplate_name, {"liquorListAlmostOut" : liquorListAlmostOut})


# function for creating the liquor list page, to show off liquor inventory
def liquorList(request):
    template_name = "liquorList.html"

    # creating a list of liquor objects from the SQLite db
    liquorList = [];
    liquorList = Liquor.objects.all().order_by('name')
    
    form = LiquorForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/Inventory/')
    else:
        return render(request, template_name, {"liquorList" : liquorList, "form": form})
    

# The function to display a single item for the liquor list.
def liquorItem(request, pk):
    liquorItem = Liquor.objects.get(pk=pk)

    form = updateLiquorForm(request.POST or None, instance=liquorItem)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/Inventory/')

    else:
        print(form.errors)
        return render(request, "liquorItem.html", {"liquorItem":liquorItem, "form": form})
    
def deleteItem(request, pk):
    liquorItem = Liquor.objects.get(pk=pk)
    liquorItem.delete()
    return HttpResponseRedirect("/Inventory/")