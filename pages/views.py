from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from agents.models import Agent
from listings.choices import *


# Create your views here.
def index(request):
    property = Listing.objects.filter(is_published=True).filter(is_featured=True)
    top_property = Listing.objects.filter(is_published=True).filter(is_top_property=True)
    agents = Agent.objects.all()
    
    if request.method == "GET":
        context ={
            "prop": property,
            "topprop": top_property,
            "agents":agents,
            "contract": contract,
            "city": city,
            "bath": Bath,
            "bed": Bed,
            "price": Price
        }

        print(Listing.CITY)

    return render(request, 'pages/index.html', context)
