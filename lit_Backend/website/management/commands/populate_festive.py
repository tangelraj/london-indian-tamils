from datetime import date

from django.core.management.base import BaseCommand

from website.models import FestiveEventSection


class Command(BaseCommand):

    help = "Populate Festive Event Section"

    def handle(self, *args, **kwargs):

        FestiveEventSection.objects.get_or_create(

            id=1,

            defaults={

                "title": (
                    "A Festive Day Out for the Whole Family!"
                ),

                "description": (
                    "Shop, explore and soak in the magic "
                    "of Christmas at the Bath Christmas Market. "
                    "See the flier and watch the video "
                    "for all the details."
                ),

                "flyer_button_text": "View the full flier",

                "video_button_text": "Watch the video",

                "booking_title": (
                    "Book Your Seat Today - Limited Seats!"
                ),

                "event_date": date(2026, 12, 12),

                "pickup_details": (
                    "Pick-up: Hillingdon Station 9:00 AM "
                    "& M4 Reading Services 9:30 AM"
                ),

                "price": "£15 per person including children",

                "button_text": "BOOK NOW",

                "button_link": "",

                "instagram_text": "Follow LIT on",

                "instagram_username": "@londonindiantamils",

                "instagram_link": (
                    "https://www.instagram.com/londonindiantamils/"
                ),

                "is_active": True,

            }

        )

        self.stdout.write(
            self.style.SUCCESS(
                "Festive Event Section populated successfully!"
            )
        )