from django.core.management.base import BaseCommand

from website.models import FounderSection


class Command(BaseCommand):

    help = "Populate Founder Section"

    def handle(self, *args, **kwargs):

        FounderSection.objects.get_or_create(

            id=1,

            defaults={

                "name": "Sathish Duraisamy",

                "designation": (
                    "Founder & Director, London Indian Tamils"
                ),

                "description_one": (
                    "London Indian Tamils was founded by "
                    "Sathish Duraisamy with a simple vision - "
                    "to create a stronger, more connected and "
                    "supportive community for Tamil-speaking "
                    "Indians living across the UK."
                ),

                "description_two": (
                    "Having lived in the UK for many years "
                    "and been actively involved in community, "
                    "cultural and social initiatives, Sathish "
                    "wanted to create a platform that goes "
                    "beyond events and WhatsApp conversations - "
                    "a community where people can build "
                    "friendships, support careers and businesses, "
                    "share opportunities and celebrate Tamil "
                    "culture together."
                ),

                "description_three": (
                    "Sathish has been involved in community "
                    "and cultural initiatives in the UK for "
                    "many years. He previously served as "
                    "Secretary of the South Indian Society "
                    "(SIS) and is also the Founder & Director "
                    "of I for India and E for Events, through "
                    "which he has organised and supported "
                    "a wide range of Indian cultural, social "
                    "and entertainment activities in the UK."
                ),

                "description_four": (
                    "His vision for LIT is to bring people "
                    "together across generations, professions "
                    "and locations, creating meaningful "
                    "connections and a community that "
                    "supports one another."
                ),

                "quote": (
                    "LIT is about people, relationships and "
                    "creating something valuable for the "
                    "community - together."
                ),

                "button_text": "ABOUT SATHISH",

                "button_link": "#founder",

                "is_active": True,

            }

        )

        self.stdout.write(
            self.style.SUCCESS(
                "Founder section populated successfully!"
            )
        )