#!/usr/bin/python
#coding=utf-8
from django.contrib.syndication.feeds import Feed
from lizproj.myblog.models import Entry
from django.utils.feedgenerator import Atom1Feed
from django.contrib.syndication.feeds import FeedDoesNotExist
####http://www.djangoproject.com/documentation/syndication_feeds/

class MyRssFeed(Feed):
    title = "Lizziesky Blog"
    link = "/lizziesky/"
    description = "Liz Blog"

    #def link(self, obj):
	#if not obj:
		#raise FeedDoesNotExist
        #return obj.get_absolute_url()
    def items(self):
        return Entry.objects.order_by('-pub_date')[:10]

class AtomFeed(MyRssFeed):
    feed_type = Atom1Feed
    subtitle = MyRssFeed.description
