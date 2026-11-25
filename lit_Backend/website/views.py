from django.shortcuts import render, redirect

from .forms import MembershipApplicationForm

from .models import (
    WebsiteSettings,
    NavigationLink,
    HeroSection,
    FloatingButton,
    AboutSection,
    AboutFeature,
    FounderSection,
    CommunitySection,
    CommunityCard,
    EventsSection,
    Event,
    FestiveEventSection,
    PastEventSection,
    EventHighlightSection,
    VoicesSection,
    VoiceMessage,
    JoinSection,
    JoinBenefit,
    SocialMediaSection,
    SocialMediaLink,
    ContactSection,
    ContactButton,
    FooterSection,
    FooterSocialLink,
    FooterPolicyLink,
)


# ==========================================
# HOME PAGE
# ==========================================

def home(request):

    context = {

        # Website Settings

        "website": WebsiteSettings.objects.first(),

        # Navigation

        "navigation_links": NavigationLink.objects.filter(
            is_active=True
        ).order_by("order"),

        # Hero Section

        "hero": HeroSection.objects.first(),

        # Floating Buttons

        "floating_buttons": FloatingButton.objects.filter(
            is_active=True
        ).order_by("order"),

        # About Section

        "about": AboutSection.objects.first(),

        "about_features": AboutFeature.objects.filter(
            is_active=True
        ).order_by("order"),

        # Founder Section

        "founder": FounderSection.objects.filter(
            is_active=True
        ).first(),

        # Community Section

        "community": CommunitySection.objects.filter(
            is_active=True
        ).first(),

        "community_cards": CommunityCard.objects.filter(
            is_active=True
        ).order_by("order", "id"),

        # Events Section

        "events_section": EventsSection.objects.filter(
            is_active=True
        ).first(),

        "events": Event.objects.filter(
            is_active=True
        ).order_by("order", "id"),

        # Festive Event Section

        "festive": FestiveEventSection.objects.filter(
            is_active=True
        ).first(),

        # Past Events Section

        "past_events": PastEventSection.objects.filter(
            is_active=True
        ).order_by("order", "id"),

        # Event Highlights Section

        "event_highlights": EventHighlightSection.objects.filter(
            is_active=True
        ).order_by("order", "id"),

        # Voices of Support Section

        "voices_section": VoicesSection.objects.filter(
            is_active=True
        ).first(),

        "voice_messages": VoiceMessage.objects.filter(
            is_active=True
        ).order_by("order", "id"),

        # Join LIT Section

        "join_section": JoinSection.objects.filter(
            is_active=True
        ).first(),

        "join_benefits": JoinBenefit.objects.filter(
            is_active=True
        ).order_by("order", "id"),

        # Social Media Section

        "social_section": SocialMediaSection.objects.filter(
            is_active=True
        ).first(),

        "social_links": SocialMediaLink.objects.filter(
            is_active=True
        ).order_by("order", "id"),

        # Contact Section

        "contact_section": ContactSection.objects.filter(
            is_active=True
        ).first(),

        "contact_buttons": ContactButton.objects.filter(
            is_active=True
        ).order_by("order", "id"),

        # Footer Section

        "footer_section": FooterSection.objects.filter(
            is_active=True
        ).first(),

        "footer_social_links": FooterSocialLink.objects.filter(
            is_active=True
        ).order_by("order", "id"),

        "footer_policy_links": FooterPolicyLink.objects.filter(
            is_active=True
        ).order_by("order", "id"),

    }

    return render(request, "index.html", context)


# ==========================================
# MEMBERSHIP REGISTRATION PAGE
# ==========================================

def join_membership(request):

    if request.method == "POST":

        form = MembershipApplicationForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("membership_success")

    else:

        form = MembershipApplicationForm()

    context = {
        "form": form,
        "website": WebsiteSettings.objects.first(),
    }

    return render(
        request,
        "membership_form.html",
        context
    )


# ==========================================
# MEMBERSHIP SUCCESS PAGE
# ==========================================

def membership_success(request):

    context = {
        "website": WebsiteSettings.objects.first(),
    }

    return render(
        request,
        "membership_success.html",
        context
    )