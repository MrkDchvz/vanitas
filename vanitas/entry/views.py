from django.shortcuts import render
from .models import Entry, Mood
# Create your views here.
def index(request):
    entries =  Entry.objects.order_by('date_created')
    return render(request, 'entry/index.html', {'entries' : entries})


def form(request):
    moods = Mood.objects.all()
    return render(request, 'entry/form.html', {'moods' : moods})
