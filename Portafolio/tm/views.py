from django.shortcuts import render, HttpResponse

# Create your views here.

def house(request):
    return render(request, 'tm/house.html')
