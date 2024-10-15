from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person
from .forms import PersonForm


def index(request):
    return render(request, 'index.html')


@login_required
def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'person.html', context={
        'persons' : persons
    })


@login_required
def persons_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('persons_list')
    return render(request, 'person_form.html', context={
        'form': form
    })


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, id=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('persons_list')
    return render(request, 'person_form.html', context={
        'form': form
    })


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, id=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    if request.method == 'POST':
        person.delete()
        return redirect('persons_list')
    return render(request, 'person_delete_confirm.html', context={
        'person': person
    })

