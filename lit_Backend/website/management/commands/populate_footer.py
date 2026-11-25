from django.core.management.base import BaseCommand

from website.models import (
    FooterSection,
    FooterSocialLink,
    FooterPolicyLink,
)


class Command(BaseCommand):

    help = "Populate Footer Section"

    def handle(self, *args, **kwargs):

        # ==================================
        # FOOTER MAIN CONTENT
        # ==================================

        FooterSection.objects.get_or_create(
            id=1,
            defaults={
                "title": "LONDON INDIAN TAMILS",

                "tagline": (
                    "CONNECT • SUPPORT • CELEBRATE"
                ),

                "description": (
                    "India in our heart. "
                    "London in our home. "
                    "Tamil in our identity."
                ),

                "copyright_text": (
                    "© 2026 London Indian Tamils. "
                    "All Rights Reserved."
                ),

                "developer_text": (
                    "Designed & Developed by"
                ),

                "developer_name": "Vetri IT Systems",

                "developer_url": "",

                "is_active": True,
            }
        )

        # ==================================
        # SOCIAL MEDIA ICONS
        # ==================================

        social_links = [
            {
                "name": "Facebook",
                "icon": "fa-brands fa-facebook-f",
                "url": "",
                "order": 1,
            },
            {
                "name": "Instagram",
                "icon": "fa-brands fa-instagram",
                "url": (
                    "https://www.instagram.com/"
                    "londonindiantamils/"
                ),
                "order": 2,
            },
        ]

        for social in social_links:

            FooterSocialLink.objects.get_or_create(
                name=social["name"],
                defaults={
                    "icon": social["icon"],
                    "url": social["url"],
                    "order": social["order"],
                    "is_active": True,
                }
            )

        # ==================================
        # POLICY LINKS
        # ==================================

        policies = [
            "Privacy Policy",
            "Community Guidelines",
            "Cookie settings",
        ]

        for index, title in enumerate(
            policies,
            start=1
        ):

            FooterPolicyLink.objects.get_or_create(
                title=title,
                defaults={
                    "link": "",
                    "order": index,
                    "is_active": True,
                }
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Footer section populated successfully!"
            )
        )