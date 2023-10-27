from django.contrib import admin
from django.urls import path

from core.views import index, about
from userprofile.views import SignUp

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),

    # signup
    path('sign-up/', SignUp, name='signup'),
    path("admin/", admin.site.urls),
]
