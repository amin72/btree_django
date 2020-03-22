from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


def contact(request):
    if request.method == 'POST':
        listing = request.POST.get('listing')
        listing_id = request.POST.get('listing_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        user_id = request.POST.get('user_id')
        realtor_email = request.POST.get('realtor_email')

        print(listing, listing_id, name, email, phone, message, user_id, realtor_email)

        Contact.objects.create(listing=listing,
            listing_id=listing_id,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id)

        messages.success(request, "Your request has been submitted,"\
            "a realtor will get back to you soon")
        
        return redirect('listings:listing', listing_id)