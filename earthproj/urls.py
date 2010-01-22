# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from ragendja.urlsauto import urlpatterns
from ragendja.auth.urls import urlpatterns as auth_patterns
from django.contrib import admin
import os

admin.autodiscover()

handler500 = 'ragendja.views.server_error'
urlpatterns = auth_patterns + patterns('',
    ('^admin/(.*)', admin.site.root),
    #(r'^guestbook/', include("guestbook.urls")),
    (r'^blog/', include("earth.urls")),
    #(r'^$', 'django.views.generic.simple.direct_to_template',
    #    {'template': 'main.html'}),
) + urlpatterns
