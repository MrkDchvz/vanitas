from django.shortcuts import get_object_or_404, render
from .models import Entry, Mood
from .forms import PostForm
# Create your views here.
def index(request):
    entries =  Entry.objects.order_by('date_created')
    return render(request, 'entry/index.html', {'entries' : entries})


def add_entry(request):
    form = PostForm()
    moods = Mood.objects.all()
    return render(request, 'entry/add_entry.html', {'moods' : moods, 'form' : form})

def detail(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    return render(request, 'entry/detail.html', {'entry' : entry})
