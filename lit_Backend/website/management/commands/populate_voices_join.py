from django.core.management.base import BaseCommand

from website.models import (
    VoicesSection,
    VoiceMessage,
    JoinSection,
    JoinBenefit,
)


class Command(BaseCommand):

    help = "Populate Voices and Join sections"

    def handle(self, *args, **kwargs):

        # ==================================
        # VOICES SECTION
        # ==================================

        VoicesSection.objects.get_or_create(
            id=1,
            defaults={
                "eyebrow": "VOICES OF SUPPORT",

                "title": "Messages to the",

                "highlighted_title": "LIT Community",

                "description": (
                    "We're grateful to have received special "
                    "messages of support and encouragement for "
                    "London Indian Tamils from respected "
                    "personalities from the Tamil community."
                ),

                "instagram_text": "Follow",

                "instagram_username": "@londonindiantamils",

                "instagram_description": (
                    "for more community stories, "
                    "messages and updates."
                ),

                "instagram_url": (
                    "https://www.instagram.com/londonindiantamils/"
                ),

                "is_active": True,
            }
        )

        # ==================================
        # VOICE MESSAGE CARDS
        # ==================================

        messages = [
            {
                "name": "Srinivas",
                "designation": "Singer",
                "order": 1,
            },
            {
                "name": "Unni Krishnan",
                "designation": "Singer",
                "order": 2,
            },
            {
                "name": "Gopinath",
                "designation": "Neeya Naana",
                "order": 3,
            },
            {
                "name": "Dushyanth Sridhar",
                "designation": "Speaker & Author",
                "order": 4,
            },
        ]

        for message in messages:

            VoiceMessage.objects.get_or_create(
                name=message["name"],
                defaults={
                    "designation": message["designation"],
                    "order": message["order"],
                    "button_text": "Watch Message",
                    "video_url": "",
                    "is_active": True,
                }
            )

        # ==================================
        # JOIN SECTION
        # ==================================

        JoinSection.objects.get_or_create(
            id=1,
            defaults={
                "title": "Join",

                "highlighted_title": (
                    "London Indian Tamils"
                ),

                "description": (
                    "Tamil-speaking Indian living in the UK?"
                ),

                "sub_description": (
                    "Become part of our growing community."
                ),

                "button_text": "JOIN NOW",

                "button_link": "",

                "is_active": True,
            }
        )

        # ==================================
        # JOIN BENEFITS
        # ==================================

        benefits = [
            "Connect with people",
            "Make friends",
            "Find opportunities",
            "Support businesses",
            "Attend events",
            "Celebrate together",
        ]

        for index, title in enumerate(benefits, start=1):

            JoinBenefit.objects.get_or_create(
                title=title,
                defaults={
                    "order": index,
                    "is_active": True,
                }
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Voices and Join sections populated successfully!"
            )
        )