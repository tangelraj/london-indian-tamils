from django.core.management.base import BaseCommand
from website.models import (
    WebsiteSettings,
    NavigationLink,
    HeroSection,
    FloatingButton,
)


class Command(BaseCommand):
    help = "Populate default LIT website content"

    def handle(self, *args, **kwargs):

        WebsiteSettings.objects.get_or_create(id=1)

        HeroSection.objects.get_or_create(id=1)

        navigation_links = [
            ("About", "#about"),
            ("Founder", "#founder"),
            ("Community", "#community"),
            ("Events", "#events"),
            ("Voices", "#voices"),
            ("Join LIT", "#join"),
            ("Contact", "#contact"),
        ]

        for index, (title, link) in enumerate(
            navigation_links, start=1
        ):
            NavigationLink.objects.get_or_create(
                title=title,
                defaults={
                    "link": link,
                    "order": index,
                    "is_active": True,
                }
            )

        floating_buttons = [
            {
                "title": "Phone",
                "icon": "phone",
                "link": "",
                "background_color": "#E3A63B",
                "order": 1,
            },
            {
                "title": "Email",
                "icon": "mail",
                "link": "",
                "background_color": "#701D25",
                "order": 2,
            },
            {
                "title": "Instagram",
                "icon": "instagram",
                "link": "",
                "background_color": "#C13584",
                "order": 3,
            },
        ]

        for button in floating_buttons:
            FloatingButton.objects.get_or_create(
                title=button["title"],
                defaults={
                    "icon": button["icon"],
                    "link": button["link"],
                    "background_color": button["background_color"],
                    "order": button["order"],
                    "is_active": True,
                }
            )

        self.stdout.write(
            self.style.SUCCESS(
                "LIT website content populated successfully!"
            )
        )