"""Defines URL patterns for learning_logs"""

from django.urls import re_path as url

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),

    # Show all topics.
    url(r'^topics/$', views.topics, name='topics'),

    # Detail page for a single topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic')
]
