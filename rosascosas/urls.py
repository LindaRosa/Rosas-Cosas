from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rosascosas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^transcribe/$', 'callme.views.transcribe_incoming', name='transcribe_incoming'),
    url(r'^playback/$', 'callme.views.playback', name='playback'),
    url(r'^admin/', include(admin.site.urls)),
)
