from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
	allProds = []
	catprods = Product.objects.values('category','id')
	cats = {item['category'] for item in catprods}
	for cat in cats:
		prod = Product.objects.filter(category=cat)
		n = len(prod)
		nslides = n//2 + ceil((n/4)-(n//4))
		allProds.append([prod, range(1,nslides), nslides])
	context = {'allProds': allProds}
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

