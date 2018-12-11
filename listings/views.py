from django.shortcuts import render

from .models import Listing

# Create your views here.
def index(req):
    listings = Listing.objects.all()
    context = {
        'listings':listings
    }
    return render(req, 'listings/listings.html', context)

def listing(req, listing_id):
    return render(req, 'listings/listing.html')

def search(req):
    return render(req, 'listings/search.html')