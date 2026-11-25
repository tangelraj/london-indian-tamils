from datetime import date

from django.core.management.base import BaseCommand

from website.models import PastEventSection


class Command(BaseCommand):

    help = "Populate existing past events"

    def handle(self, *args, **kwargs):

        PastEventSection.objects.get_or_create(

            id=1,

            defaults={

                "title": (
                    "Deepavali Kondattam – An Evening of "
                    "Music, Nostalgia & Celebration"
                ),

                "event_date": date(2026, 10, 31),

                "location": "London",

                "introduction": (
                    "An unforgettable evening of music, "
                    "memories and togetherness!"
                ),

                "description": (
                    "London Indian Tamils (LIT) celebrated "
                    "Deepavali with a wonderful musical evening "
                    "featuring singer M J Shriram, bringing "
                    "the magic of Tamil cinema’s golden musical "
                    "era to life.\n\n"

                    "The evening was filled with much-loved "
                    "songs, particularly the timeless musical "
                    "combinations of S. P. Balasubrahmanyam "
                    "(SPB) and Ilaiyaraaja. These evergreen "
                    "classics brought back beautiful memories, "
                    "with audiences singing along and reliving "
                    "the music that has touched generations.\n\n"

                    "A special highlight was M J Shriram’s "
                    "energetic performance, entertaining the "
                    "audience with nearly 3.5 hours of non-stop "
                    "singing. His wit, humour and engaging "
                    "interaction made the evening as entertaining "
                    "as it was nostalgic.\n\n"

                    "Beyond the music, it was a wonderful "
                    "opportunity for families and friends to "
                    "come together, celebrate Deepavali and "
                    "enjoy the warmth of our Tamil community.\n\n"

                    "Our heartfelt thanks to M J Shriram, "
                    "everyone who attended, and all our "
                    "supporters and volunteers who helped "
                    "make this celebration memorable."
                ),

                "quote": (
                    "A night of songs, smiles and memories "
                    "that will stay with us for a long time!"
                ),

                "gallery_title": "Relive the Moments",

                "gallery_description": (
                    "Explore the photographs from our Deepavali "
                    "Kondattam and revisit the special moments "
                    "from the evening."
                ),

                "organisation_name": (
                    "London Indian Tamils (LIT)"
                ),

                "tagline": (
                    "CONNECT • SUPPORT • CELEBRATE"
                ),

                "button_text": (
                    "VIEW THE EVENT PHOTO GALLERY"
                ),

                "button_link": "",

                "order": 1,

                "is_active": True,

            }

        )

        self.stdout.write(
            self.style.SUCCESS(
                "Past Event Section populated successfully!"
            )
        )