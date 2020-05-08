from django.shortcuts import render
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def index(request):
    property = Listing.objects.order_by('-list_date')
    paginator = Paginator(property,10)
    page = request.GET.get('page')
    paged_property = paginator.get_page(page)

    if request.method == "GET":
        context ={
            "prop": paged_property
        }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')