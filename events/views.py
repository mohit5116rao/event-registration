from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Event
from .forms import EventForm

# Create your views here.


def event_list(request):
    queryset = Event.objects.all()
    context = {
        'object_list': queryset,
    }

    return render(request, 'events/list.html', context)

def event_create(request):
    form = EventForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('/')

    context = {
        'form': form,
    }

    return render(request, 'events/create.html', context)
