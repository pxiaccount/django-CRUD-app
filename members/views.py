from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member
from django.urls import reverse

# Create your views here.
def index(request):
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render())
    products = Member.objects.all()
    return render(request, 'index.html', {
        'products': products
    })

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def add_to_model(request):
    name = request.POST['name']
    age = request.POST['age']
    member = Member(name=name, age=age)
    member.save()
    return HttpResponseRedirect(reverse('index'))

def remove_model(request, id):
    model = Member.objects.get(id=id)
    model.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    model = Member.objects.get(id=id)
    # template = loader.get_template('update.html')
    return render(request, 'update.html', {
        'model': model
    })

def update_to_model(request, id):
    name = request.POST['name']
    age = request.POST['age']
    model = Member.objects.get(id=id)
    model.name = name
    model.age = age
    model.save()
    return HttpResponseRedirect(reverse('index'))