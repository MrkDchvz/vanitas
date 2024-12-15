from django.core.management.base import BaseCommand
from entry.models import Mood, Entry  
from django.utils import timezone
import random

class Command(BaseCommand):
    help = "Generate 10 custom entries based on random moods"

    def handle(self, *args, **kwargs):
        # Fetch all moods from the database
        moods = Mood.objects.all()
        if not moods.exists():
            self.stdout.write("No moods found in the database. Please add moods first!")
            return

        # Define example titles and content templates
        example_titles = [
            "A Day to Remember",
            "The Joy of Life",
            "Overcoming Challenges",
            "Reflections on the Week",
            "Moments of Gratitude",
            "An Unexpected Journey",
        ]

        example_contents = [
            "Today was a rollercoaster of emotions, but I felt particularly {mood}.",
            "It's been a {mood} kind of day, full of unexpected surprises.",
            "Sometimes, being {mood} can teach us important lessons about life.",
            "I had a {mood} moment today, and it was truly unforgettable.",
            "Feeling {mood} reminds me to stay grounded and appreciate the little things.",
        ]

       
        entries_to_create = []
        # Change this number to generate desired number of post ('Default: 10')
        number_of_post_to_create = 10;
    
        for _ in range(number_of_post_to_create):
            mood = random.choice(moods)  # Randomly pick a mood
            title = random.choice(example_titles)
            content = random.choice(example_contents).format(mood=mood.name.lower())
            entry = Entry(
                mood=mood,
                title=title,
                content=content,
                date_created=timezone.now(),
            )
            entries_to_create.append(entry)

        # Bulk create the entries
        Entry.objects.bulk_create(entries_to_create)

        self.stdout.write("10 entries generated successfully!")
