from django.conf.urls.defaults import *
from lizproj.myblog.my_feeds import MyRssFeed, AtomFeed

feeds={
	'rss':MyRssFeed,
	'atom':AtomFeed,
}
urlpatterns = patterns('',
    (r'^$', 'newlizproj.myblog.views.show_frontpage'),
    (r'^post/(?P<post_id>\d{1})/$', 'newlizproj.myblog.views.get_post'),
    (r'^cmtsave/$', 'newlizproj.myblog.views.save_comment'), 
    (r'^edit/', 'newlizproj.myblog.views.edit'),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict':feeds}),
	(r'^aboutme/$', 'newlizproj.myblog.views.aboutme'),
	(r'^date/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<year>\d{4})/$','newlizproj.myblog.views.get_posts_by_date'),
    (r'^tag/(?P<tagname>.*)/$', 'newlizproj.myblog.views.get_posts_by_tag'),
    (r'^search/', 'newlizproj.myblog.views.search_blog'),
    )
#    (r'^wb/$','write_blog'),
#    (r'^save/$','save'),   
#    (r'^premonth/$','premonth'), 
#    (r'^nextmonth/$','nextmonth'),
#    (r'^monthtitle/$','monthtitle'),
#    (r'^date/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$','get_posts_by_date'),
#    (r'date/(?P<time>\d{4}-\d{2})','get_archiver'),
#    (r'^savetotxt/$', 'save_txt'),
#    (r'^post/(?P<post_id>.*)/$', 'get_post'),
#    (r'^save_comment/$','save_comment'), cmtsave/
#    (r'category/(?P<cate>\S*)/$','list_category'),
