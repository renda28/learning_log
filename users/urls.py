"""Defines URL patterns for users"""


from django.urls import include
from django.urls import re_path as url
from django.contrib.auth.views import LoginView

from . import views


app_name = 'users'

urlpatterns = [
    # Login page
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
    # Logout page
    url(r'^logout/$', views.logout_view, name='logout'),
]
