from django.conf.urls.defaults import *

urlpatterns = patterns('earth.views',
    (r'^$', 'index'),
    #(r'^post/(?P<post_id>\d*)/$', 'get_post'),
    #(r'^cmtsave/$', 'save_comment'), 
    #(r'^new/', 'edit'),
    #(r'^edit/(?P<post_id>\d*)/$', 'edit'),
    #(r'^save/$','save'),
    #(r'^feeds/$', 'get_feeds'),
    #(r'^feeds/comments/$', 'get_comments_feed'),
    #(r'^date/(?P<year>\d{4})/(?P<month>\d{1,2})/$','get_posts_by_ym'),
    #(r'^date/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<year>\d{4})/$', 'get_posts_by_date'),
    #(r'^tag/(?P<tagname>.*)/$', 'get_posts_by_tag'),
)