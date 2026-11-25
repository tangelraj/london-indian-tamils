from django.contrib import admin
from .models import (
    WebsiteSettings,
    NavigationLink,
    HeroSection,
    FloatingButton,
)
from .models import (
    VoicesSection,
    VoiceMessage,
    JoinSection,
    JoinBenefit,
)
from .models import (
    SocialMediaSection,
    SocialMediaLink,
    ContactSection,
    ContactButton,
)
from .models import (
    FooterSection,
    FooterSocialLink,
    FooterPolicyLink,
)
from .models import AboutSection, AboutFeature
from .models import FounderSection
from .models import CommunitySection, CommunityCard
from .models import EventsSection, Event
from .models import FestiveEventSection
from .models import PastEventSection
from .models import EventHighlightSection
from .models import MembershipApplication

admin.site.site_header = "London Indian Tamils Administration"
admin.site.site_title = "LIT Admin"
admin.site.index_title = "Website Content Management"


@admin.register(WebsiteSettings)
class WebsiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'short_name', 'tagline')

    def has_add_permission(self, request):
        return not WebsiteSettings.objects.exists() and super().has_add_permission(request)


@admin.register(NavigationLink)
class NavigationLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title',)
    list_filter = ('is_active',)


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'highlighted_title')

    def has_add_permission(self, request):
        return not HeroSection.objects.exists() and super().has_add_permission(request)


@admin.register(FloatingButton)
class FloatingButtonAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'link', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active', 'icon')

# ==========================================
# ABOUT SECTION ADMIN
# ==========================================

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "highlighted_title",
        "badge_title",
    )

    fieldsets = (
        ("Section Heading", {
            "fields": (
                "eyebrow",
                "title",
                "highlighted_title",
            )
        }),

        ("Description", {
            "fields": (
                "description",
                "secondary_description",
            )
        }),

        ("Section Images", {
            "fields": (
                "image",
                "background_image",
            )
        }),

        ("Community Badge", {
            "fields": (
                "badge_title",
                "badge_subtitle",
            )
        }),
    )

    def has_add_permission(self, request):

        if AboutSection.objects.exists():
            return False

        return super().has_add_permission(request)


# ==========================================
# ABOUT FEATURES ADMIN
# ==========================================

@admin.register(AboutFeature)
class AboutFeatureAdmin(admin.ModelAdmin):

    list_display = (
        "number",
        "title",
        "icon",
        "order",
        "is_active",
    )

    list_editable = (
        "order",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
        "description",
    )

    ordering = (
        "order",
        "id",
    )

    # ==========================================
# FOUNDER SECTION ADMIN
# ==========================================

@admin.register(FounderSection)
class FounderSectionAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "designation",
        "is_active",
    )

    list_editable = (
        "is_active",
    )

    search_fields = (
        "name",
        "designation",
    )

    fieldsets = (

        ("Founder Information", {
            "fields": (
                "name",
                "designation",
                "image",
            )
        }),

        ("Founder Biography", {
            "fields": (
                "description_one",
                "description_two",
                "description_three",
                "description_four",
            )
        }),

        ("Founder Quote", {
            "fields": (
                "quote",
            )
        }),

        ("Button Settings", {
            "fields": (
                "button_text",
                "button_link",
            )
        }),

        ("Section Settings", {
            "fields": (
                "background_image",
                "is_active",
            )
        }),

    )

    def has_add_permission(self, request):

        if FounderSection.objects.exists():
            return False

        return super().has_add_permission(request)

    # ==========================================
# COMMUNITY SECTION ADMIN
# ==========================================

@admin.register(CommunitySection)
class CommunitySectionAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "highlighted_title",
        "is_active",
    )

    list_editable = (
        "is_active",
    )

    fieldsets = (

        ("Section Content", {
            "fields": (
                "top_text",
                "eyebrow",
                "title",
                "highlighted_title",
            )
        }),

        ("Section Settings", {
            "fields": (
                "background_image",
                "is_active",
            )
        }),

    )

    def has_add_permission(self, request):

        if CommunitySection.objects.exists():
            return False

        return super().has_add_permission(request)


# ==========================================
# COMMUNITY CARDS ADMIN
# ==========================================

@admin.register(CommunityCard)
class CommunityCardAdmin(admin.ModelAdmin):

    list_display = (
        "number",
        "title",
        "icon",
        "order",
        "is_highlighted",
        "is_active",
    )

    list_editable = (
        "order",
        "is_highlighted",
        "is_active",
    )

    list_filter = (
        "is_active",
        "is_highlighted",
    )

    search_fields = (
        "title",
        "description",
    )

    ordering = (
        "order",
        "id",
    )

    fieldsets = (

        ("Card Content", {
            "fields": (
                "number",
                "title",
                "description",
            )
        }),

        ("Card Icon", {
            "fields": (
                "icon",
                "custom_icon",
            )
        }),

        ("Card Settings", {
            "fields": (
                "order",
                "is_highlighted",
                "is_active",
            )
        }),

    )

    # ==========================================
# EVENTS SECTION ADMIN
# ==========================================

@admin.register(EventsSection)
class EventsSectionAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "highlighted_title",
        "is_active",
    )

    list_editable = ("is_active",)

    fieldsets = (

        ("Section Heading", {
            "fields": (
                "eyebrow",
                "title",
                "highlighted_title",
            )
        }),

        ("Section Content", {
            "fields": (
                "description",
                "categories",
            )
        }),

        ("Section Settings", {
            "fields": (
                "background_image",
                "is_active",
            )
        }),

    )

    def has_add_permission(self, request):

        if EventsSection.objects.exists():
            return False

        return super().has_add_permission(request)


# ==========================================
# EVENT ADMIN
# ==========================================

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "event_date",
        "price",
        "order",
        "is_active",
    )

    list_editable = (
        "order",
        "is_active",
    )

    list_filter = (
        "is_active",
        "event_date",
    )

    search_fields = (
        "title",
        "subtitle",
        "pickup_details",
    )

    ordering = ("order", "id")

    fieldsets = (

        ("Event Heading", {
            "fields": (
                "badge_text",
                "title",
                "subtitle",
                "year",
                "image",
            )
        }),

        ("Event Details", {
            "fields": (
                "event_date",
                "pickup_details",
                "price",
                "price_note",
            )
        }),

        ("Booking Button", {
            "fields": (
                "button_text",
                "button_link",
            )
        }),

        ("Event Settings", {
            "fields": (
                "order",
                "is_active",
            )
        }),

    )

# ==========================================
# FESTIVE EVENT SECTION ADMIN
# ==========================================

@admin.register(FestiveEventSection)
class FestiveEventSectionAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "event_date",
        "price",
        "is_active",
    )

    list_editable = ("is_active",)

    fieldsets = (

        ("Section Heading", {
            "fields": (
                "title",
                "description",
            )
        }),

        ("Event Flyer", {
            "fields": (
                "flyer_image",
                "flyer_button_text",
            )
        }),

        ("Event Video", {
            "fields": (
                "video_thumbnail",
                "video_file",
                "video_url",
                "video_button_text",
            )
        }),

        ("Booking Details", {
            "fields": (
                "booking_title",
                "event_date",
                "pickup_details",
                "price",
                "button_text",
                "button_link",
            )
        }),

        ("Instagram Settings", {
            "fields": (
                "instagram_text",
                "instagram_username",
                "instagram_link",
            )
        }),

        ("Section Settings", {
            "fields": (
                "is_active",
            )
        }),

    )

    def has_add_permission(self, request):

        if FestiveEventSection.objects.exists():
            return False

        return super().has_add_permission(request)

    # ==========================================
# PAST EVENT SECTION ADMIN
# ==========================================

@admin.register(PastEventSection)
class PastEventSectionAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "event_date",
        "location",
        "order",
        "is_active",
    )

    list_editable = (
        "order",
        "is_active",
    )

    search_fields = (
        "title",
        "location",
        "description",
    )

    fieldsets = (

        ("Event Heading", {
            "fields": (
                "title",
                "event_date",
                "location",
            )
        }),

        ("Event Content", {
            "fields": (
                "introduction",
                "description",
                "quote",
            )
        }),

        ("Photo Gallery", {
            "fields": (
                "gallery_title",
                "gallery_description",
                "organisation_name",
                "tagline",
                "button_text",
                "button_link",
            )
        }),

        ("Section Settings", {
            "fields": (
                "order",
                "is_active",
            )
        }),

    )

    # ==========================================
# EVENT HIGHLIGHTS ADMIN
# ==========================================

@admin.register(EventHighlightSection)
class EventHighlightSectionAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "event_date",
        "location",
        "order",
        "is_active",
    )

    list_editable = (
        "order",
        "is_active",
    )

    search_fields = (
        "title",
        "description",
        "location",
    )

    fieldsets = (

        ("Section Heading", {
            "fields": (
                "title",
                "description",
            )
        }),

        ("Highlights Video", {
            "fields": (
                "thumbnail",
                "video_url",
                "video_button_text",
            )
        }),

        ("Event Gallery", {
            "fields": (
                "gallery_title",
                "event_date",
                "location",
                "gallery_button_text",
                "gallery_url",
            )
        }),

        ("Instagram Settings", {
            "fields": (
                "instagram_text",
                "instagram_username",
                "instagram_url",
            )
        }),

        ("Section Settings", {
            "fields": (
                "order",
                "is_active",
            )
        }),

    )

    # ==========================================
# VOICES SECTION ADMIN
# ==========================================

@admin.register(VoicesSection)
class VoicesSectionAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "highlighted_title",
        "is_active",
    )

    list_editable = ("is_active",)


@admin.register(VoiceMessage)
class VoiceMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "designation",
        "order",
        "is_active",
    )

    list_editable = (
        "order",
        "is_active",
    )

    search_fields = (
        "name",
        "designation",
    )


# ==========================================
# JOIN SECTION ADMIN
# ==========================================

@admin.register(JoinSection)
class JoinSectionAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "highlighted_title",
        "is_active",
    )

    list_editable = ("is_active",)


@admin.register(JoinBenefit)
class JoinBenefitAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "order",
        "is_active",
    )

    list_editable = (
        "order",
        "is_active",
    )

    # ==========================================
# SOCIAL MEDIA ADMIN
# ==========================================

@admin.register(SocialMediaSection)
class SocialMediaSectionAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "highlighted_title",
        "is_active",
    )

    list_editable = ("is_active",)


@admin.register(SocialMediaLink)
class SocialMediaLinkAdmin(admin.ModelAdmin):

    list_display = (
        "platform",
        "display_name",
        "url",
        "order",
        "is_active",
    )

    list_editable = (
        "order",
        "is_active",
    )

    search_fields = (
        "platform",
        "display_name",
    )


# ==========================================
# CONTACT SECTION ADMIN
# ==========================================

@admin.register(ContactSection)
class ContactSectionAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "email",
        "phone",
        "is_active",
    )

    list_editable = ("is_active",)


@admin.register(ContactButton)
class ContactButtonAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "icon",
        "link",
        "order",
        "is_active",
    )

    list_editable = (
        "order",
        "is_active",
    )

    # ==========================================
# FOOTER SECTION ADMIN
# ==========================================

@admin.register(FooterSection)
class FooterSectionAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "developer_name",
        "is_active",
    )

    list_editable = ("is_active",)


# ==========================================
# FOOTER SOCIAL LINKS ADMIN
# ==========================================

@admin.register(FooterSocialLink)
class FooterSocialLinkAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "icon",
        "url",
        "order",
        "is_active",
    )

    list_editable = (
        "order",
        "is_active",
    )

    search_fields = ("name",)


# ==========================================
# FOOTER POLICY LINKS ADMIN
# ==========================================

@admin.register(FooterPolicyLink)
class FooterPolicyLinkAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "link",
        "order",
        "is_active",
    )

    list_editable = (
        "order",
        "is_active",
    )

    search_fields = ("title",)

    @admin.register(MembershipApplication)
    class MembershipApplicationAdmin(admin.ModelAdmin):

        list_display = (
            "name",
            "email",
            "postcode",
            "phone",
            "submitted_at",
            "is_approved",
        )

        list_editable = ("is_approved",)

        search_fields = (
            "name",
            "email",
            "postcode",
            "phone",
        )

        list_filter = (
            "is_approved",
            "submitted_at",
        )

        readonly_fields = ("submitted_at",)

        list_per_page = 25