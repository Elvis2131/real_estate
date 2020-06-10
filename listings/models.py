from django.db import models
from datetime import datetime
from agents.models import Agent

# Create your models here.
class Listing(models.Model):

    CONTRACT_TYPE=(
        ('RENT','RENT'),
        ('SALE','SALE')
    )

    CITY = (
        ('Accra','Accra'),
        ('Kumasi','Kumasi'),
        ('Takoradi','Takoradi')
    )

    agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50, choices=CITY, blank=False)
    description = models.TextField(max_length=500)
    property_type = models.CharField(max_length=500)
    reference = models.CharField(max_length=50)
    price = models.IntegerField()
    bathroom = models.IntegerField()
    room = models.IntegerField()
    bed = models.IntegerField()
    garage = models.IntegerField()
    garage_area = models.DecimalField(max_digits=4, decimal_places=1)
    home_area = models.DecimalField(max_digits=4, decimal_places=1)
    lot_area = models.DecimalField(max_digits=4, decimal_places=1)
    parking_lot = models.IntegerField()
    contract = models.CharField(max_length=10, choices=CONTRACT_TYPE, default='SALE')
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    
    # images model
    main_image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    feature_image_1 = models.ImageField(upload_to='photos/property/%Y/%m/%d/', blank=True, default="photos/default/default.jpg")
    feature_image_2 = models.ImageField(upload_to='photos/property/%Y/%m/%d/', blank=True, default="photos/default/default.jpg")

    """
    Other Property info
    """ 
    is_featured = models.BooleanField(default=False)
    is_top_property = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

