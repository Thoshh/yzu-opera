#!/usr/bin/python
#coding=utf-8
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render_to_response

def index(request):
    return render_to_response("blog/index.html")
