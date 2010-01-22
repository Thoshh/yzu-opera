# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response
from earth.models import *
import datetime
#from django.core.paginator import ObjectPaginator, InvalidPage
from google.appengine.ext import db
from google.appengine.api import users
from django.utils.feedgenerator import Rss201rev2Feed, Atom1Feed

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.list_detail import object_list
from django.views.generic.create_update import create_object
from django.contrib.auth.decorators import login_required
from settings import MY_MEDIA_URL

ENTRYNUM_ONEPAGE = 3
TAG_DEFAULT_SIZE = 15
TAG_DEFAULT_STEP = 6
SIMILARITY = 0.2

SITE_PARAM = {'MEDIA_URL': MY_MEDIA_URL}
def index(request):
    """显示首页
    """
    all_entry = Entry.all().order('-date')
    return render_to_response("earth/main.html", {
            'entry_list': all_entry,
            'SITE_PARAM': SITE_PARAM,
            })

def get_posts_by(request, different_entry, all_entry):
    """获得不同的entry并分页显示, 还有其他一些数据
    """
    # 所有Entry的分页显示
    paginator = ObjectPaginator(different_entry, ENTRYNUM_ONEPAGE)
    try:
        # 获得对应页面
        page = int(request.GET.get('page', '1'))
        entry = paginator.get_page(page-1)
    except  InvalidPage:
        raise Http404
    return render_to_response("blog/main.html", {
                'entry_list': entry,
                'has_next': paginator.has_next_page(page - 1),
                'has_previous': paginator.has_previous_page(page - 1),
                'next_page': page + 1,
                'previous_page': page - 1,
                "all_cat":_get_tag_count(),
                "all_arch":_get_arch(),
                'all_links': Links.all(),
                'head_title': MYTITLE,
                'page_url': request.get_full_path()[1:],
                })

