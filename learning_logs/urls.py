"""Defines URL patterns for learning_logs"""

from django.urls import re_path as url

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
]