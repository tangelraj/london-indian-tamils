from datetime import date

from django.core.management.base import BaseCommand

from website.models import EventHighlightSection


class Command(BaseCommand):

    help = "Populate Event Highlights Section"

    def handle(self, *args, **kwargs):

        EventHighlightSection.objects.get_or_create(

            id=1,

            defaults={

                "title": "Deepavali Kondattam Highlights",

                "description": (
                    "Relive the music, colour and celebration "
                    "from our Deepavali Kondattam evening."
                ),

                "video_url": "",

                "video_button_text": (
                    "Watch the highlights on Instagram"
                ),

                "gallery_title": (
                    "Thank You for Celebrating With Us"
                ),

                "event_date": date(2026, 10, 31),

                "location": "Cranford Suite, TW5 9PD",

                "gallery_button_text": (
                    "VIEW THE EVENT PHOTO GALLERY"
                ),

                "gallery_url": "",

                "instagram_text": "Watch more from LIT on",

                "instagram_username": "@londonindiantamils",

                "instagram_url": (
                    "https://www.instagram.com/londonindiantamils/"
                ),

                "order": 1,

                "is_active": True,

            }

        )

        self.stdout.write(
            self.style.SUCCESS(
                "Event Highlights Section populated successfully!"
            )
        )