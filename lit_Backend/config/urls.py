from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.views.static import serve


# ==========================================
# URL CONFIGURATION
# ==========================================

urlpatterns = [

    # ======================================
    # DJANGO ADMIN PANEL
    # ======================================

    path("admin/", admin.site.urls),


    # ======================================
    # ADMIN UPLOADED PUBLIC MEDIA FILES
    # Supports local development and Render
    # ======================================

    re_path(
        r"^media/(?P<path>.*)$",
        serve,
        {
            "document_root": settings.MEDIA_ROOT,
            "show_indexes": False,
        },
    ),


    # ======================================
    # WEBSITE FRONTEND URLS
    # ======================================

    path("", include("website.urls")),

]