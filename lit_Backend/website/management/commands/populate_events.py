from datetime import date

from django.core.management.base import BaseCommand

from website.models import EventsSection, Event


class Command(BaseCommand):

    help = "Populate LIT Events Section"

    def handle(self, *args, **kwargs):

        EventsSection.objects.get_or_create(

            id=1,

            defaults={

                "eyebrow": "EVENTS",

                "title": "Meet. Celebrate.",

                "highlighted_title": "Connect.",

                "description": (
                    "LIT brings our online community together "
                    "through real-world experiences."
                ),

                "categories": (
                    "Social Meet-ups • Live Music • "
                    "Cultural Events • Open Mic • "
                    "Family Activities • Sports • "
                    "Networking • Day Trips • Festivals"
                ),

                "is_active": True,

            }
        )

        Event.objects.get_or_create(

            id=1,

            defaults={

                "badge_text": "FEATURED EVENT",

                "title": "Christmas Market:",

                "subtitle": "Bath Day Trip",

                "year": "2026",

                "event_date": date(2026, 12, 12),

                "pickup_details": (
                    "Pick-up 9:00 AM at Hillingdon Station "
                    "and 9:30 AM at M4 Reading Services Westbound"
                ),

                "price": "£15 per person including children",

                "price_note": "(food and drinks not included.)",

                "button_text": "BOOK NOW",

                "button_link": "",

                "order": 1,

                "is_active": True,

            }
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Events section populated successfully!"
            )
        )