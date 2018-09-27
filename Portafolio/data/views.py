from django.shortcuts import render, HttpResponse,redirect
from data.models import Project
from data.forms import formulario
from django.urls import reverse


# Create your views here.
def portfolio(request):
    return render(request, 'data/portfolio.html')

def person(request):
    people=Project.objects.all()
    return render(request, 'data/person.html',{"people":people})

def addproject(request):
    project_form=formulario()

    if request.mothod == "POST":
         project_form=formulario(request.POST, request.FILES)
         if project_form.is_valid():
             projecto = Project()
             projecto.title = request.POST.get("title")
             projecto.description = request.POST.get("description")
             projecto.image = request.POST.get("image")
             projecto.link= request.POST.get("link")
             projecto.save()

             return redirect(reversed("person"))
    return render(request, 'data/addproject.html',{"form":project_form})