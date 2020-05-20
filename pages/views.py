from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from agents.models import Agent


# Create your views here.
def index(request):
    property = Listing.objects.filter(is_published=True).filter(is_featured=True)
    top_property = Listing.objects.filter(is_published=True).filter(is_top_property=True)
    agents = Agent.objects.all()
    
    if request.method == "GET":
        context ={
            "prop": property,
            "topprop": top_property,
            "agents":agents
        }

    return render(request, 'pages/index.html', context)
