from django.shortcuts import get_object_or_404, render
from .models import Entry, Mood
# Create your views here.
def index(request):
    entries =  Entry.objects.order_by('date_created')
    return render(request, 'entry/index.html', {'entries' : entries})


def form(request):
    moods = Mood.objects.all()
    return render(request, 'entry/form.html', {'moods' : moods})

def detail(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    return render(request, 'entry/detail.html', {'entry' : entry})
