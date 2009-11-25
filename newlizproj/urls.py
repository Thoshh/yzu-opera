from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^blog/', include('newlizproj.myblog.urls')),
    (r'^$', 'newlizproj.views.index'),

    # Uncomment this for admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_PATH}),
)
