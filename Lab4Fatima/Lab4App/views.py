from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

tax_rate= 15

def defaultPath(request):
    return HttpResponse("This is a site to calculate tax.")

def priceCalculation(request, num):
    
    totPrice = num + (num*(tax_rate/100))

    return HttpResponse(f"the total price after 15% tax: {totPrice}")

def taxrate(request):
    
    return render(request, 'taxrate.html', {'tax_rate': tax_rate}) 

