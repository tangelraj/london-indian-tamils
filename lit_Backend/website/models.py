from django.db import models


class WebsiteSettings(models.Model):
    logo = models.ImageField(
        upload_to='website/',
        blank=True
    )
    site_name = models.CharField(
        max_length=200,
        default="London Indian Tamils"
    )
    short_name = models.CharField(
        max_length=50,
        default="(LIT)"
    )
    tagline = models.CharField(
        max_length=200,
        default="CONNECT • SUPPORT • CELEBRATE"
    )
    description = models.CharField(
        max_length=300,
        default="India in our heart. London in our home. Tamil in our identity."
    )
    button_text = models.CharField(
        max_length=100,
        default="JOIN LIT"
    )
    button_link = models.CharField(
        max_length=500,
        default="#join"
    )

    class Meta:
        verbose_name_plural = "Website Settings"

    def __str__(self):
        return self.site_name


class NavigationLink(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=500)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class HeroSection(models.Model):
    badge_text = models.CharField(
        max_length=200,
        default="LONDON • தமிழ் • INDIA • UK"
    )
    title = models.CharField(
        max_length=300,
        default="Connecting Indian Tamils Across"
    )
    highlighted_title = models.CharField(
        max_length=200,
        default="London & the UK"
    )
    description = models.TextField(
        default="London Indian Tamils (LIT) is a growing community bringing together Tamil-speaking people of Indian origin living across the UK."
    )
    sub_description = models.TextField(
        default="Meet people. Make friends. Discover opportunities. Support one another. Celebrate our culture."
    )
    background_image = models.ImageField(
        upload_to='hero/',
        blank=True
    )
    primary_button_text = models.CharField(
        max_length=100,
        default="JOIN LIT"
    )
    primary_button_link = models.CharField(
        max_length=500,
        default="#join"
    )
    secondary_button_text = models.CharField(
        max_length=100,
        default="VIEW EVENTS"
    )
    secondary_button_link = models.CharField(
        max_length=500,
        default="#events"
    )

    class Meta:
        verbose_name_plural = "Hero Section"

    def __str__(self):
        return self.title


class FloatingButton(models.Model):

    ICON_CHOICES = [
        ('phone', 'Phone'),
        ('mail', 'Email'),
        ('instagram', 'Instagram'),
        ('whatsapp', 'WhatsApp'),
        ('facebook', 'Facebook'),
    ]

    title = models.CharField(max_length=100)
    icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES
    )
    link = models.CharField(max_length=500)
    background_color = models.CharField(
        max_length=100,
        default="#E3A63B"
    )
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

        # ==========================================
# ABOUT SECTION
# ==========================================

class AboutSection(models.Model):

    eyebrow = models.CharField(
        max_length=100,
        default="ABOUT LIT"
    )

    title = models.CharField(
        max_length=250,
        default="More Than a WhatsApp Group."
    )

    highlighted_title = models.CharField(
        max_length=150,
        default="A Community."
    )

    description = models.TextField()

    secondary_description = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to="about/",
        blank=True,
        null=True
    )

    background_image = models.ImageField(
        upload_to="about/backgrounds/",
        blank=True,
        null=True
    )

    badge_title = models.CharField(
        max_length=100,
        default="தமிழ்"
    )

    badge_subtitle = models.CharField(
        max_length=100,
        default="ONE COMMUNITY"
    )

    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Section"

    def __str__(self):
        return self.title


# ==========================================
# ABOUT FEATURE CARDS
# ==========================================

class AboutFeature(models.Model):

    ICON_CHOICES = [
        ("fa-solid fa-users", "Connect"),
        ("fa-solid fa-handshake-angle", "Support"),
        ("fa-solid fa-wand-magic-sparkles", "Celebrate"),
        ("fa-solid fa-heart", "Heart"),
        ("fa-solid fa-globe", "Globe"),
        ("fa-solid fa-star", "Star"),
        ("fa-solid fa-handshake", "Handshake"),
    ]

    number = models.CharField(
        max_length=10,
        default="01"
    )

    title = models.CharField(
        max_length=150
    )

    description = models.TextField()

    icon = models.CharField(
        max_length=100,
        choices=ICON_CHOICES,
        default="fa-solid fa-users"
    )

    order = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "About Feature"
        verbose_name_plural = "About Features"

    def __str__(self):
        return self.title

    # ==========================================
# FOUNDER SECTION
# ==========================================

class FounderSection(models.Model):

    name = models.CharField(
        max_length=200,
        default="Sathish Duraisamy"
    )

    designation = models.CharField(
        max_length=250,
        default="Founder & Director, London Indian Tamils"
    )

    image = models.ImageField(
        upload_to="founder/",
        blank=True,
        null=True
    )

    description_one = models.TextField()

    description_two = models.TextField(
        blank=True
    )

    description_three = models.TextField(
        blank=True
    )

    description_four = models.TextField(
        blank=True
    )

    quote = models.TextField(
        blank=True
    )

    button_text = models.CharField(
        max_length=100,
        default="ABOUT SATHISH"
    )

    button_link = models.CharField(
        max_length=500,
        default="#founder",
        blank=True
    )

    background_image = models.ImageField(
        upload_to="founder/backgrounds/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        verbose_name = "Founder Section"
        verbose_name_plural = "Founder Section"

    def __str__(self):
        return self.name

    # ==========================================
# COMMUNITY SECTION
# ==========================================

class CommunitySection(models.Model):

    top_text = models.CharField(
        max_length=500,
        default=(
            "A growing UK community • Social • Careers • "
            "Business • Sports • Families • Marketplace • Events"
        )
    )

    eyebrow = models.CharField(
        max_length=100,
        default="OUR COMMUNITY"
    )

    title = models.CharField(
        max_length=200,
        default="There's Something"
    )

    highlighted_title = models.CharField(
        max_length=200,
        default="for Everyone"
    )

    background_image = models.ImageField(
        upload_to="community/backgrounds/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Community Section"
        verbose_name_plural = "Community Section"

    def __str__(self):
        return self.title


# ==========================================
# COMMUNITY CARDS
# ==========================================

class CommunityCard(models.Model):

    ICON_CHOICES = [
        ("fa-solid fa-users", "Social"),
        ("fa-solid fa-briefcase", "Jobs & Careers"),
        ("fa-solid fa-store", "Business"),
        ("fa-solid fa-bag-shopping", "Marketplace"),
        ("fa-solid fa-bullhorn", "Politics"),
        ("fa-solid fa-trophy", "Sports"),
        ("fa-solid fa-graduation-cap", "Education"),
        ("fa-solid fa-calendar-check", "Events"),
        ("fa-solid fa-heart", "Heart"),
        ("fa-solid fa-globe", "Globe"),
        ("fa-solid fa-star", "Star"),
    ]

    number = models.CharField(
        max_length=10,
        default="01"
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    icon = models.CharField(
        max_length=100,
        choices=ICON_CHOICES,
        default="fa-solid fa-users"
    )

    custom_icon = models.ImageField(
        upload_to="community/icons/",
        blank=True,
        null=True
    )

    is_highlighted = models.BooleanField(
        default=False
    )

    order = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Community Card"
        verbose_name_plural = "Community Cards"

    def __str__(self):
        return self.title

    # ==========================================
# EVENTS SECTION
# ==========================================

class EventsSection(models.Model):

    eyebrow = models.CharField(
        max_length=100,
        default="EVENTS"
    )

    title = models.CharField(
        max_length=200,
        default="Meet. Celebrate."
    )

    highlighted_title = models.CharField(
        max_length=200,
        default="Connect."
    )

    description = models.TextField(
        default=(
            "LIT brings our online community together "
            "through real-world experiences."
        )
    )

    categories = models.TextField(
        default=(
            "Social Meet-ups • Live Music • Cultural Events • "
            "Open Mic • Family Activities • Sports • "
            "Networking • Day Trips • Festivals"
        )
    )

    background_image = models.ImageField(
        upload_to="events/backgrounds/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Events Section"
        verbose_name_plural = "Events Section"

    def __str__(self):
        return self.title


# ==========================================
# EVENT CARDS
# ==========================================

class Event(models.Model):

    badge_text = models.CharField(
        max_length=100,
        default="FEATURED EVENT"
    )

    title = models.CharField(max_length=250)

    subtitle = models.CharField(
        max_length=250,
        blank=True
    )

    year = models.CharField(
        max_length=20,
        default="2026"
    )

    image = models.ImageField(
        upload_to="events/",
        blank=True,
        null=True
    )

    event_date = models.DateField()

    pickup_details = models.TextField(blank=True)

    price = models.CharField(max_length=250)

    price_note = models.CharField(
        max_length=250,
        blank=True
    )

    button_text = models.CharField(
        max_length=100,
        default="BOOK NOW"
    )

    button_link = models.CharField(
        max_length=500,
        blank=True
    )

    order = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.title

    # ==========================================
# FESTIVE EVENT DETAILS SECTION
# ==========================================

class FestiveEventSection(models.Model):

    title = models.CharField(
        max_length=250,
        default="A Festive Day Out for the Whole Family!"
    )

    description = models.TextField(
        default=(
            "Shop, explore and soak in the magic of Christmas "
            "at the Bath Christmas Market. See the flier "
            "and watch the video for all the details."
        )
    )

    flyer_image = models.ImageField(
        upload_to="festive/flyers/",
        blank=True,
        null=True
    )

    flyer_button_text = models.CharField(
        max_length=100,
        default="View the full flier"
    )

    video_thumbnail = models.ImageField(
        upload_to="festive/thumbnails/",
        blank=True,
        null=True
    )

    video_file = models.FileField(
        upload_to="festive/videos/",
        blank=True,
        null=True
    )

    video_url = models.URLField(
        max_length=500,
        blank=True
    )

    video_button_text = models.CharField(
        max_length=100,
        default="Watch the video"
    )

    booking_title = models.CharField(
        max_length=250,
        default="Book Your Seat Today - Limited Seats!"
    )

    event_date = models.DateField()

    pickup_details = models.CharField(
        max_length=500,
        default=(
            "Pick-up: Hillingdon Station 9:00 AM "
            "& M4 Reading Services 9:30 AM"
        )
    )

    price = models.CharField(
        max_length=250,
        default="£15 per person including children"
    )

    button_text = models.CharField(
        max_length=100,
        default="BOOK NOW"
    )

    button_link = models.URLField(
        max_length=500,
        blank=True
    )

    instagram_text = models.CharField(
        max_length=100,
        default="Follow LIT on"
    )

    instagram_username = models.CharField(
        max_length=100,
        default="@londonindiantamils"
    )

    instagram_link = models.URLField(
        max_length=500,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Festive Event Section"
        verbose_name_plural = "Festive Event Section"

    def __str__(self):
        return self.title

    # ==========================================
# PAST EVENT SECTION
# ==========================================

class PastEventSection(models.Model):

    title = models.CharField(max_length=300)

    event_date = models.DateField()

    location = models.CharField(
        max_length=200,
        default="London"
    )

    introduction = models.TextField()

    description = models.TextField()

    quote = models.TextField(blank=True)

    gallery_title = models.CharField(
        max_length=200,
        default="Relive the Moments"
    )

    gallery_description = models.TextField()

    organisation_name = models.CharField(
        max_length=200,
        default="London Indian Tamils (LIT)"
    )

    tagline = models.CharField(
        max_length=200,
        default="CONNECT • SUPPORT • CELEBRATE"
    )

    button_text = models.CharField(
        max_length=150,
        default="VIEW THE EVENT PHOTO GALLERY"
    )

    button_link = models.URLField(
        max_length=500,
        blank=True
    )

    order = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Past Event Section"
        verbose_name_plural = "Past Event Sections"

    def __str__(self):
        return self.title

    # ==========================================
# EVENT HIGHLIGHTS SECTION
# ==========================================

class EventHighlightSection(models.Model):

    title = models.CharField(max_length=250)

    description = models.TextField()

    thumbnail = models.ImageField(
        upload_to="highlights/thumbnails/",
        blank=True,
        null=True
    )

    video_url = models.URLField(
        max_length=500,
        blank=True
    )

    video_button_text = models.CharField(
        max_length=200,
        default="Watch the highlights on Instagram"
    )

    gallery_title = models.CharField(
        max_length=250,
        default="Thank You for Celebrating With Us"
    )

    event_date = models.DateField()

    location = models.CharField(max_length=250)

    gallery_button_text = models.CharField(
        max_length=200,
        default="VIEW THE EVENT PHOTO GALLERY"
    )

    gallery_url = models.URLField(
        max_length=500,
        blank=True
    )

    instagram_text = models.CharField(
        max_length=200,
        default="Watch more from LIT on"
    )

    instagram_username = models.CharField(
        max_length=100,
        default="@londonindiantamils"
    )

    instagram_url = models.URLField(
        max_length=500,
        blank=True
    )

    order = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Event Highlight Section"
        verbose_name_plural = "Event Highlight Sections"

    def __str__(self):
        return self.title

    # ==========================================
# VOICES OF SUPPORT SECTION
# ==========================================

class VoicesSection(models.Model):

    eyebrow = models.CharField(
        max_length=150,
        default="VOICES OF SUPPORT"
    )

    title = models.CharField(
        max_length=200,
        default="Messages to the"
    )

    highlighted_title = models.CharField(
        max_length=200,
        default="LIT Community"
    )

    description = models.TextField()

    instagram_text = models.CharField(
        max_length=250,
        default="Follow"
    )

    instagram_username = models.CharField(
        max_length=100,
        default="@londonindiantamils"
    )

    instagram_description = models.CharField(
        max_length=250,
        default="for more community stories, messages and updates."
    )

    instagram_url = models.URLField(
        max_length=500,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Voices Sections"

    def __str__(self):
        return self.title


class VoiceMessage(models.Model):

    name = models.CharField(max_length=200)

    designation = models.CharField(max_length=200)

    image = models.ImageField(
        upload_to="voices/",
        blank=True
    )

    button_text = models.CharField(
        max_length=100,
        default="Watch Message"
    )

    video_url = models.URLField(
        max_length=500,
        blank=True
    )

    order = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.name


# ==========================================
# JOIN LIT SECTION
# ==========================================

class JoinSection(models.Model):

    title = models.CharField(
        max_length=200,
        default="Join"
    )

    highlighted_title = models.CharField(
        max_length=200,
        default="London Indian Tamils"
    )

    description = models.TextField(
        default="Tamil-speaking Indian living in the UK?"
    )

    sub_description = models.TextField(
        default="Become part of our growing community."
    )

    background_image = models.ImageField(
        upload_to="join/",
        blank=True
    )

    button_text = models.CharField(
        max_length=100,
        default="JOIN NOW"
    )

    button_link = models.CharField(
        max_length=500,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Join Sections"

    def __str__(self):
        return "Join London Indian Tamils"


class JoinBenefit(models.Model):

    title = models.CharField(max_length=200)

    order = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title

    # ==========================================
# SOCIAL MEDIA SECTION
# ==========================================

class SocialMediaSection(models.Model):

    eyebrow = models.CharField(
        max_length=150,
        default="SOCIAL MEDIA"
    )

    title = models.CharField(
        max_length=200,
        default="Stay Connected"
    )

    highlighted_title = models.CharField(
        max_length=200,
        default="With LIT"
    )

    description = models.TextField()

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Social Media Sections"

    def __str__(self):
        return self.title


class SocialMediaLink(models.Model):

    platform = models.CharField(max_length=100)

    display_name = models.CharField(max_length=200)

    icon = models.CharField(
        max_length=100,
        default="fa-brands fa-instagram"
    )

    url = models.URLField(
        max_length=500,
        blank=True
    )

    order = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.platform


# ==========================================
# CONTACT SECTION
# ==========================================

class ContactSection(models.Model):

    eyebrow = models.CharField(
        max_length=100,
        default="CONTACT"
    )

    title = models.CharField(
        max_length=200,
        default="London Indian Tamils"
    )

    location = models.CharField(max_length=250)

    email = models.EmailField()

    phone = models.CharField(max_length=50)

    founder_name = models.CharField(max_length=200)

    founder_designation = models.CharField(
        max_length=200,
        default="Founder & Director"
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Contact Sections"

    def __str__(self):
        return self.title


class ContactButton(models.Model):

    title = models.CharField(max_length=100)

    icon = models.CharField(max_length=100)

    link = models.CharField(
        max_length=500,
        blank=True
    )

    order = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title

    # ==========================================
# FOOTER SECTION
# ==========================================

class FooterSection(models.Model):

    title = models.CharField(
        max_length=200,
        default="LONDON INDIAN TAMILS"
    )

    tagline = models.CharField(
        max_length=250,
        default="CONNECT • SUPPORT • CELEBRATE"
    )

    description = models.TextField(
        default=(
            "India in our heart. London in our home. "
            "Tamil in our identity."
        )
    )

    copyright_text = models.CharField(
        max_length=300,
        default=(
            "© 2026 London Indian Tamils. "
            "All Rights Reserved."
        )
    )

    developer_text = models.CharField(
        max_length=200,
        default="Designed & Developed by"
    )

    developer_name = models.CharField(
        max_length=200,
        default="Vetri IT Systems"
    )

    developer_url = models.URLField(
        max_length=500,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Footer Sections"

    def __str__(self):
        return self.title


# ==========================================
# FOOTER SOCIAL MEDIA ICONS
# ==========================================

class FooterSocialLink(models.Model):

    name = models.CharField(max_length=100)

    icon = models.CharField(max_length=100)

    url = models.URLField(
        max_length=500,
        blank=True
    )

    order = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.name


# ==========================================
# FOOTER POLICY LINKS
# ==========================================

class FooterPolicyLink(models.Model):

    title = models.CharField(max_length=200)

    link = models.CharField(
        max_length=500,
        blank=True
    )

    order = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title

    # ==========================================
# COMMUNITY MEMBERSHIP REGISTRATION
# ==========================================

class MembershipApplication(models.Model):

    email = models.EmailField()

    name = models.CharField(max_length=200)

    postcode = models.CharField(
        max_length=20,
        verbose_name="Post Code Area"
    )

    phone = models.CharField(max_length=30)

    submitted_at = models.DateTimeField(
        auto_now_add=True
    )

    is_approved = models.BooleanField(
        default=False
    )

    class Meta:
        ordering = ["-submitted_at"]
        verbose_name = "Membership Application"
        verbose_name_plural = "Membership Applications"

    def __str__(self):
        return self.name