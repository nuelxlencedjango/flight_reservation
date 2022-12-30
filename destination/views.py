
from django.shortcuts import render
from bs4 import BeautifulSoup as bs
from urllib import request
import re
import pandas as pd
from datetime import datetime
# Create your views here.

import urllib.request



def indexPage(request):

    minDate = f"{datetime.now().date().year}-{datetime.now().date().month}-{datetime.now().date().day}"
    maxDate = f"{datetime.now().date().year if (datetime.now().date().month+3)<=12 else datetime.now().date().year+1}-{(datetime.now().date().month + 3) if (datetime.now().date().month+3)<=12 else (datetime.now().date().month+3-12)}-{datetime.now().date().day}"
    if request.method == 'POST':

        origin = request.POST.get('takeOff')
        destination = request.POST.get('destination')
        depart_date = request.POST.get('takeOffDate')
        seat = request.POST.get('SeatClass')
        trip_type = request.POST.get('TripType')

        if(trip_type == 'oneWay'):
            context ={'takeOff': origin,'destination': destination,'depart_date': depart_date,
            'seat': seat.lower(),'trip_type': trip_type}

            return render(request, 'flights/index.html', context)


        elif(trip_type == 'roundTrip'):
    
            return_date = request.POST.get('returnDate')

            context = {'min_date': minDate,
            'max_date': maxDate,
            'takeOff': origin, 
            'destination': destination,
            'depart_date': depart_date,
            'seat': seat.lower(),
            'trip_type': trip_type,
            'return_date': return_date,
            }
           
            return render(request, 'flights/index.html', context)
              
    else:
        return render(request, 'flights/index.html', {
            'min_date': minDate,
            'max_date': maxDate,
           
        })

