from django.shortcuts import render
from listings.models import Listing


def index(request):
    listings = Listing.objects.filter(is_published=True) \
        .order_by('-list_date')[:3]
    
    context = {
        'listings': listings,
        'home_active': True
    }
    return render(request, "pages/index.html", context)



def about(request):
    context = {
        'about_active': True
    }
    return render(request, "pages/about.html", context)
