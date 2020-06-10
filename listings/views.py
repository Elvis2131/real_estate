from django.shortcuts import render
from .models import Listing
from agents.models import Agent
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    property = Listing.objects.order_by('-list_date').filter(is_published=True)
    agents = Agent.objects.all()
    paginator = Paginator(property,10)
    page = request.GET.get('page')
    paged_property = paginator.get_page(page)

    if request.method == "GET":
        context ={
            "prop": paged_property,
            "agents": agents,
        }
    
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    property = Listing.objects.get(pk=listing_id)
    agents = Agent.objects.all()
    if request.method == "GET":
        context={
            "property":property,
            "agents":agents
        }

    return render(request, 'listings/listing.html', context)

def search(request):
    return render(request, 'listings/search.html')