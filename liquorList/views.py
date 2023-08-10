from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Liquor

from .forms import LiquorForm

# Function for creating the home page.
def home(request):
    hometemplate_name = "home.html"

    liquorListAlmostOut = Liquor.objects.filter(numberOfBottles__lt=3)

    return render(request, hometemplate_name, {"liquorListAlmostOut" : liquorListAlmostOut})


# function for creating the liquor list page, to show off liquor inventory
def liquorList(request):
    template_name = "liquorList.html"
    appName = request.GET.get("name") or "liquor List"

    # creating a list of liquor objects from the SQLite db
    liquorList = [];
    liquorList = Liquor.objects.all().order_by('name')
    
    form = LiquorForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/Inventory/')
    else:
        return render(request, template_name, {"appName" : appName, "liquorList" : liquorList, "form": form})
  
