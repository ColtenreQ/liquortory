from django.shortcuts import render

def aboutPage(request):
    template_name = "about_page.html"

    return render(request, template_name)