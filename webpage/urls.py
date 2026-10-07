from django.urls import path

from . import views

app_name = "webpage"


urlpatterns = [
    path("imprint", views.ImprintView.as_view(), name="imprint"),
    path("about", views.AboutView.as_view(), name="about"),
    path("index", views.IndexView.as_view(), name="index"),
    path("", views.IndexView.as_view(), name="start"),
    path("accounts/login/", views.user_login, name="user_login"),
    path("logout/", views.user_logout, name="user_logout"),
]
