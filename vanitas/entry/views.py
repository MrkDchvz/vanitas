from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EntryForm
from .models import Entry, Mood
# Create your views here.
def index(request):
    entries =  Entry.objects.order_by('date_created')
    return render(request, 'entry/index.html', {'entries' : entries})


def detail(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    return render(request, 'entry/detail.html', {'entry' : entry})

def add_entry(request):
    if request.method == "POST":
        # Instead of saving the form create an entry model Instance w/ values that the user entered from POST Request
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.title = form.cleaned_data['title']  # Access form data for title
            entry.mood = form.cleaned_data['mood']    # Access form data for mood
            entry.content = form.cleaned_data['content']
            entry.date_created = timezone.now()
            entry.save()

            return HttpResponseRedirect(reverse('entry:detail', args=(entry.pk,)))
    else:
        form = EntryForm()
        moods = Mood.objects.all()
    return render(request, 'entry/add_entry.html', {'moods' : moods, 'form' : form})