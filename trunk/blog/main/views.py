# -*- encoding:utf-8 -*-
import sys,os

reload(sys)
sys.setdefaultencoding('utf-8')

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.utils.http import urlquote
from django.contrib.auth.models import AnonymousUser
import settings

def index(request):
    """Ê×Ò³
    """
    ruser = request.user
    return HttpResponse('hi')