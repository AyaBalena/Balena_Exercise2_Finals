# account/urls.py
from django.urls import path
from . views import (
    sign_up,
    login_view,
    logout_view,
    password_reset_request,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
)