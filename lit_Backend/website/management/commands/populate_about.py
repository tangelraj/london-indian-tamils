from django.core.management.base import BaseCommand

from website.models import (
    AboutSection,
    AboutFeature,
)


class Command(BaseCommand):

    help = "Populate About LIT section"

    def handle(self, *args, **kwargs):

        AboutSection.objects.get_or_create(

            id=1,

            defaults={

                "eyebrow": "ABOUT LIT",

                "title": "More Than a WhatsApp Group.",

                "highlighted_title": "A Community.",

                "description": (
                    "London Indian Tamils (LIT) is a growing "
                    "community bringing together Tamil-speaking "
                    "people of Indian origin living across the UK "
                    "– a place to meet people, make friends, "
                    "discover opportunities, support one another "
                    "and celebrate our culture."
                ),

                "secondary_description": (
                    "A place to build friendships, share "
                    "opportunities, support businesses and careers, "
                    "celebrate our culture and participate in "
                    "social, educational, sporting and community "
                    "activities."
                ),

                "badge_title": "தமிழ்",

                "badge_subtitle": "ONE COMMUNITY",

            }
        )

        features = [

            {
                "number": "01",
                "title": "Connect",
                "description": (
                    "Meet people, make friends and build "
                    "personal and professional connections."
                ),
                "icon": "fa-solid fa-users",
                "order": 1,
            },

            {
                "number": "02",
                "title": "Support",
                "description": (
                    "Share opportunities, support careers "
                    "and businesses and help one another."
                ),
                "icon": "fa-solid fa-handshake-angle",
                "order": 2,
            },

            {
                "number": "03",
                "title": "Celebrate",
                "description": (
                    "Celebrate our Tamil language, Indian roots, "
                    "culture, festivals, music, food and traditions."
                ),
                "icon": "fa-solid fa-wand-magic-sparkles",
                "order": 3,
            },

        ]

        for feature in features:

            AboutFeature.objects.get_or_create(

                number=feature["number"],

                defaults={
                    "title": feature["title"],
                    "description": feature["description"],
                    "icon": feature["icon"],
                    "order": feature["order"],
                    "is_active": True,
                }
            )

        self.stdout.write(
            self.style.SUCCESS(
                "About LIT section populated successfully!"
            )
        )