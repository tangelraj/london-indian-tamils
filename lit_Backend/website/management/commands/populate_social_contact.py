from django.core.management.base import BaseCommand

from website.models import (
    SocialMediaSection,
    SocialMediaLink,
    ContactSection,
    ContactButton,
)


class Command(BaseCommand):

    help = "Populate Social Media and Contact Sections"

    def handle(self, *args, **kwargs):

        # ==================================
        # SOCIAL MEDIA SECTION
        # ==================================

        SocialMediaSection.objects.get_or_create(
            id=1,
            defaults={
                "eyebrow": "SOCIAL MEDIA",

                "title": "Stay Connected",

                "highlighted_title": "With LIT",

                "description": (
                    "Follow us for community news, "
                    "event announcements, photos, "
                    "videos and activities."
                ),

                "is_active": True,
            }
        )

        # ==================================
        # SOCIAL MEDIA LINKS
        # ==================================

        social_links = [
            {
                "platform": "INSTAGRAM",
                "display_name": "@londonindiantamils",
                "icon": "fa-brands fa-instagram",
                "url": (
                    "https://www.instagram.com/"
                    "londonindiantamils/"
                ),
                "order": 1,
            },
            {
                "platform": "FACEBOOK",
                "display_name": "London Indian Tamils",
                "icon": "fa-brands fa-facebook-f",
                "url": "",
                "order": 2,
            },
        ]

        for item in social_links:

            SocialMediaLink.objects.get_or_create(
                platform=item["platform"],
                defaults={
                    "display_name": item["display_name"],
                    "icon": item["icon"],
                    "url": item["url"],
                    "order": item["order"],
                    "is_active": True,
                }
            )

        # ==================================
        # CONTACT SECTION
        # ==================================

        ContactSection.objects.get_or_create(
            id=1,
            defaults={
                "eyebrow": "CONTACT",

                "title": "London Indian Tamils",

                "location": "London, United Kingdom",

                "email": "londonindiantamils@gmail.com",

                "phone": "07940 173183",

                "founder_name": "Sathish Duraisamy",

                "founder_designation": (
                    "Founder & Director"
                ),

                "is_active": True,
            }
        )

        # ==================================
        # CONTACT BUTTONS
        # ==================================

        buttons = [
            {
                "title": "CALL",
                "icon": "fa-solid fa-phone",
                "link": "tel:+447940173183",
                "order": 1,
            },
            {
                "title": "EMAIL",
                "icon": "fa-regular fa-envelope",
                "link": (
                    "mailto:londonindiantamils@gmail.com"
                ),
                "order": 2,
            },
            {
                "title": "INSTAGRAM",
                "icon": "fa-brands fa-instagram",
                "link": (
                    "https://www.instagram.com/"
                    "londonindiantamils/"
                ),
                "order": 3,
            },
            {
                "title": "FACEBOOK",
                "icon": "fa-brands fa-facebook-f",
                "link": "",
                "order": 4,
            },
        ]

        for button in buttons:

            ContactButton.objects.get_or_create(
                title=button["title"],
                defaults={
                    "icon": button["icon"],
                    "link": button["link"],
                    "order": button["order"],
                    "is_active": True,
                }
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Social Media and Contact sections "
                "populated successfully!"
            )
        )