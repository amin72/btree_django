from django.urls import path
from . import views


app_name = 'listings'

urlpatterns = [
    # listings
    path('', views.listings, name='listings'),

    # listing
    path('<int:listing_id>/', views.listing, name='listing'),
    
    # search
    path('search/', views.search, name='search'),
]
