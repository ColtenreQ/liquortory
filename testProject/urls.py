"""
URL configuration for testProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import liquorList.views
import aboutPage.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', liquorList.views.home),
    path('about/', aboutPage.views.aboutPage),
    path('Inventory/', liquorList.views.liquorList, name="Inventory"),
    path('home/', liquorList.views.home),
    path('liquorItem/<int:pk>/', liquorList.views.liquorItem, name="liquorItem"),
    path('deleteItem/<int:pk>/', liquorList.views.deleteItem, name="deleteItem"),
    path('brands/', liquorList.views.brandList, name="brandList"),
    path('brandItem/<int:pk>/', liquorList.views.brandItem, name="brandItem")

]
