from django.shortcuts import render
from Pets.models import Pet, Owner
from Pets.forms import *
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    pets = Pet.objects.all().order_by('-votes')
    return render(request, 'index.html', {'pets': pets})


def publish(request):
    if request.method == 'POST':
        owner_form = OwnerForm(data=request.POST)
        pet_form = PetForm(data=request.POST)
        if owner_form.is_valid() and pet_form.is_valid():
            owner = owner_form.save()
            pet = pet_form.save(commit=False)
            if 'picture' in request.FILES:
                pet.picture = request.FILES['picture']
            pet.owner = owner
            pet.save()
            return HttpResponseRedirect('/')
        else:
            print owner_form.errors, pet_form.errors
    else:
        owner_form = OwnerForm()
        pet_form = PetForm()
    return render(request, 'publish.html', {'owner_form': owner_form, 'pet_form': pet_form})


def vote(request, pet_id):
    data = Pet.objects.filter(id=pet_id)
    if data.exists():
        pet = Pet.objects.get(id=pet_id)
        pet.votes += 1
        pet.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
