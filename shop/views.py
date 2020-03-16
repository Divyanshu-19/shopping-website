from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
	products = Product.objects.all()
	print(products)
	n = len(products)
	nslides = n//2 + ceil((n/4)-(n//4))
	context = {'product' : products,
			   'no_of_slides' : nslides,
			   "range": range(1,nslides)}
	return render(request,"shop/index.html",context)

def about(request):
	return render(request,"shop/about.html",{})

def contact(request):
	return HttpResponse("We are at contact")

def tracker(request):
	return HttpResponse("We are at tracker")

def search(request):
	return HttpResponse("We are at search")

def productView(request):
	return HttpResponse("We are at productView")

def checkout(request):
	return HttpResponse("We are at checkout")
