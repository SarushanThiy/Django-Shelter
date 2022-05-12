from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .forms import NewDogForm, AdoptDogForm
from .models import *
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs(request):
    data = {'doggos': Dog.objects.all()}
    return render(request, 'dogs.html', data)


@login_required
def create(request):
    if request.method == 'POST':
        dog = NewDogForm(request.POST)
        if dog.is_valid():
            id = dog.save().id
            return redirect("adoption-show", id=id)
    else:
        form = NewDogForm()
        data = {'form': form}
        return render(request, 'new.html', data)

@login_required
def show(request, id):
    dog = get_object_or_404(Dog, pk=id)
    if request.method == 'POST':
        form = AdoptDogForm(request.POST)
        if form.is_valid():
            dog.owner = request.user
            dog.save()
            return redirect("adoption-show", id=id)
    else:
        form = AdoptDogForm(initial={'owner': request.user})
    data = {
        'dog': dog,
        'form': form
    }
    return render(request, 'show.html', data)

def not_found_404(request, exception):
    return render(request, '404.html', data)

def server_error_500(request):
    return render(request, '500.html')
    