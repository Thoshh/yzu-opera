# -*- encoding:utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('blog.main.views',
    (r'^$', 'index'),
)
