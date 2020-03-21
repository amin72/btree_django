from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing


def listings(request):
    listings = Listing.objects.filter(is_published=True).order_by('-list_date')

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
        'listings_active': True
    }
    return render(request, 'listings/listings.html', context)



def listing(request, listing_id):
    context = {}
    return render(request, 'listings/listing.html', context)



def search(request):
    context = {}
    return render(request, 'listings/search.html', context)
