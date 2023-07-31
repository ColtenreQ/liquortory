from django.shortcuts import render
from .models import Liquor

# function for creating the liquor list page, to show off liquor inventory
def liquorList(request):
    template_name = "liquorList.html"
    appName = request.GET.get("name") or "liquor List"

# creating a list of liquor objects from the SQLite db
    liquorList = [];
    liquorList = Liquor.objects.all()

    return render(request, template_name, {"appName" : appName, "liquorList" : liquorList})

    

# Function for creating the home page.
def home(request):
    hometemplate_name = "home.html"

    liquorListAlmostOut = Liquor.objects.filter(numberOfBottles__lt=2)

    return render(request, hometemplate_name, {"liquorListAlmostOut" : liquorListAlmostOut})