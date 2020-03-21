from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing
from .choices import bedroom_choices, price_choices, state_choices


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
    listing = get_object_or_404(Listing, id=listing_id)

    context = {
        'listing': listing,
    }
    return render(request, 'listings/listing.html', context)



def search(request):
    keywords = request.GET.get('keywords')
    city = request.GET.get('city')
    state = request.GET.get('state')
    bedrooms = request.GET.get('bedrooms')
    price = request.GET.get('price')

    listings = Listing.objects.filter()

    if keywords:
        listings = listings.filter(description__icontains=keywords)
    
    if city:
        listings = listings.filter(city__iexact=city)
    
    if state:
        listings = listings.filter(state__iexact=state)
    
    if bedrooms:
        listings = listings.filter(bedrooms__lte=bedrooms)
    
    if price:
        listings = listings.filter(price__lte=price)

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
