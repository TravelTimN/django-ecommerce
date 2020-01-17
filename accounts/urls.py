from django.urls import include, path
from accounts import urls_reset
from accounts.views import login, logout, profile, registration


urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("profile/", profile, name="profile"),
    path("register/", registration, name="registration"),
    path("password-reset/", include(urls_reset))
]
