from django.core.management.base import BaseCommand

from website.models import (
    CommunitySection,
    CommunityCard,
)


class Command(BaseCommand):

    help = "Populate LIT Community Section"

    def handle(self, *args, **kwargs):

        CommunitySection.objects.get_or_create(

            id=1,

            defaults={

                "top_text": (
                    "A growing UK community • Social • "
                    "Careers • Business • Sports • Families • "
                    "Marketplace • Events"
                ),

                "eyebrow": "OUR COMMUNITY",

                "title": "There's Something",

                "highlighted_title": "for Everyone",

                "is_active": True,

            }
        )

        cards = [

            {
                "number": "01",
                "title": "Social",
                "description": (
                    "Meet-ups, friendships and good "
                    "times together."
                ),
                "icon": "fa-solid fa-users",
                "order": 1,
                "is_highlighted": False,
            },

            {
                "number": "02",
                "title": "Jobs & Careers",
                "description": (
                    "Openings, referrals and career guidance."
                ),
                "icon": "fa-solid fa-briefcase",
                "order": 2,
                "is_highlighted": False,
            },

            {
                "number": "03",
                "title": "Business & Networking",
                "description": (
                    "Connect, collaborate and support "
                    "businesses and professionals "
                    "within our community."
                ),
                "icon": "fa-solid fa-store",
                "order": 3,
                "is_highlighted": False,
            },

            {
                "number": "04",
                "title": "Marketplace",
                "description": (
                    "Buy, sell and recommend within "
                    "the community."
                ),
                "icon": "fa-solid fa-bag-shopping",
                "order": 4,
                "is_highlighted": False,
            },

            {
                "number": "05",
                "title": "Politics & Current Affairs",
                "description": (
                    "Respectful discussion on UK, Indian "
                    "and Tamil-related politics and "
                    "current affairs."
                ),
                "icon": "fa-solid fa-bullhorn",
                "order": 5,
                "is_highlighted": False,
            },

            {
                "number": "06",
                "title": "Sports & Fitness",
                "description": (
                    "Cricket, badminton, runs and "
                    "staying active."
                ),
                "icon": "fa-solid fa-trophy",
                "order": 6,
                "is_highlighted": False,
            },

            {
                "number": "07",
                "title": "Kids & Education",
                "description": (
                    "Tamil learning, schools and "
                    "family support."
                ),
                "icon": "fa-solid fa-graduation-cap",
                "order": 7,
                "is_highlighted": False,
            },

            {
                "number": "08",
                "title": "Events & Activities",
                "description": (
                    "Festivals, trips, music and celebrations."
                ),
                "icon": "fa-solid fa-calendar-check",
                "order": 8,
                "is_highlighted": False,
            },

        ]

        for card in cards:

            CommunityCard.objects.get_or_create(

                number=card["number"],

                defaults={

                    "title": card["title"],

                    "description": card["description"],

                    "icon": card["icon"],

                    "order": card["order"],

                    "is_highlighted": card["is_highlighted"],

                    "is_active": True,

                }

            )

        self.stdout.write(
            self.style.SUCCESS(
                "Community section populated successfully!"
            )
        )