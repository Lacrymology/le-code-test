from django.conf.urls import patterns, url
from django.views.generic import ListView

from stream.models import Stream

urlpatterns = patterns('',
    url("^$", ListView.as_view(queryset=Stream.active.all())),
)
