from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from .models import NewEntry
from .forms import EntryForm
from events.models import Event

# Create your views here.


def register_new(request):
    if request.method == 'POST':
        event_pk = request.POST.get('pk')
        event = Event.objects.get(pk=event_pk)
    else:
        event = Event.objects.filter(pk=1)
    form = EntryForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.event = event
        send_mail('Subject','this is message,you are successfully registered','mohit5116rao@gmail.com',[instance.email])
        instance.save()
        return HttpResponseRedirect('/')


    context = {
        'event': event,
        'form': form,
    }

    return  render(request, 'registration/new.html', context)

def register_list(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
    user_list=NewEntry.objects.filter(event=pk)
    context={
    'user_list':user_list,
    }

    return render(request,'registration/list.html',context)

