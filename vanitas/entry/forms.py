from django import forms
from .models import Entry, Mood
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'mood', 'content']

    # Customize field widgets with Tailwind classes
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'shadow appearance-none border rounded bg-transparent w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline',
            'placeholder': "It's time to cook! Tell us the name of thy dish",
            'required' : 'true',
        })
    )
    
    mood = forms.ModelChoiceField(
        queryset= Mood.objects.all(),  # Query the Mood model to get all choices
        empty_label=None, 
        widget=forms.Select(attrs={
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 bg-slate-950 text-white leading-tight focus:outline-none focus:shadow-outline',
            'required' : 'true',
        })
    )
    
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'shadow appearance-none border bg-transparent rounded w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline',
            'placeholder': "Let it cook! We won't tell your therapist.",
            'required' : 'true',
        })
    )