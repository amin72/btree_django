from django.shortcuts import render


def index(request):
    context = {
        'home_active': True
    }
    return render(request, "pages/index.html", context)



def about(request):
    context = {
        'about_active': True
    }
    return render(request, "pages/about.html", context)
