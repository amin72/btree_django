from django.shortcuts import render
from .models import Listing


def listings(request):
    listings = Listing.objects.all()

    context = {
        'listings': listings,
        'listings_active': True
    }
    return render(request, 'listings/listings.html', context)



def listing(request, listing_id):
    context = {}
    return render(request, 'listings/listing.html', context)



def search(request):
    context = {}
    return render(request, 'listings/search.html', context)
