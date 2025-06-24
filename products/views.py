from django.http import HttpResponse
from django.shortcuts import render
from .models import Products

# Create your views here.
def index(request):
    products_variable= Products.objects.all()
    return render(request,'index.html', {'products':products_variable})

def new(request):
    return HttpResponse('the new products')