from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path(
        "join-membership/",
        views.join_membership,
        name="join_membership"
    ),

    path(
        "membership-success/",
        views.membership_success,
        name="membership_success"
    ),
]