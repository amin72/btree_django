from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices, price_choices, state_choices


def index(request):
    listings = Listing.objects.filter(is_published=True) \
        .order_by('-list_date')[:3]
    
    context = {
        'listings': listings,
        'home_active': True,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,

    }
    return render(request, "pages/index.html", context)



def about(request):
    # get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.filter(is_mvp=True)
    
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors,
        'about_active': True
    }
    return render(request, "pages/about.html", context)
