#!/usr/bin/python
#coding=utf-8
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render_to_response
from myblog.models import Entry
from myblog.models import Tag
from myblog.models import Comment
from myblog.models import Links
import datetime
from django.views.generic.list_detail import object_list
from django.core.paginator import Paginator, InvalidPage
import random

def show_frontpage(request):
    #print request.get_full_url()
    print request.get_full_path()
    print request.path
    
    #current=datetime.date.today()
    #request.session["time"]=current
    paginator = Paginator(Entry.objects.order_by('-pub_date'), 3)
    all_entry = Entry.objects.order_by('-pub_date')
    tags=Tag.objects.all()
    comment_list=Comment.objects.order_by('-date')
    
    links = Links.objects.all()
    try:
        page = int(request.GET.get('page', '1'))
        print page
        entry = paginator.page(page).object_list
    except  InvalidPage:
        raise Http404
    return render_to_response("blog/main.html",{
            'paginator': paginator,#X
            'entry_list': entry,
            'all_entry_list': all_entry,#change to sidebar ??
            'is_paginated': paginator.num_pages > 1,
            'has_next': paginator.page(page).has_next(),
            'has_previous': paginator.page(page).has_previous(),
            'current_page': page,
            'next_page': page + 1,
            'previous_page': page - 1,
            'pages': paginator.num_pages,
           # 'hits' : paginator.hits,#X
            'page_numbers': range(paginator.num_pages+1)[1:],
            'comment_list': comment_list,#change to sidebar ??
            'tags': tags,
            #'year': current.year,
            #'month': current.month,
            'link_list': links})

#==========================================================================================
def edit(request):
    return HttpResponseRedirect("/admin")

#==========================================================================================

def aboutme(request):
    return render_to_response("blog/aboutme.html")
def save(request):#X
    post_title=request.POST.get("post_title",None)
    post_body=request.POST.get("post_body",None)
    post_tags=request.POST.get("post_tags",None)
    tags=post_tags.split(",")
    tags_db=Tag.objects.all()
    tags_db_title=[ i.title for i in tags_db ]
    for tag in tags:
        if tag.strip() in tags_db_title:
            pass
        else:
            a=Tag(slug=tag,title=tag.strip())
            a.save()
    
    try:
        entry=Entry(title=post_title,body=post_body,pub_date=datetime.datetime.now())
        entry.save()
        for tag in tags:
            b=Tag.objects.get(title=tag.strip())
            print b.title
            entry.tags.add(b)
        return HttpResponseRedirect("/blog/")
    except Exception,e:
        return HttpResponse("Write Error")

#========================================================================
def premonth(request):#X
    current=request.session["time"]
    current=current+datetime.timedelta(days=-current.day)
    request.session['time']=current
    return render_to_response("blog/_nextmonth.html",{'nian':current.year,'yue':current.month})



def nextmonth(request):#X
    current=request.session["time"]        
    if current.month==12:               
        current=datetime.date(current.year+1,1,1)        
        request.session['time']=current
    else:                                
        current=datetime.date(current.year,current.month+1,1)
        request.session['time']=current
    return render_to_response("blog/_nextmonth.html",{'nian':current.year,'yue':current.month})
#========================================================================

def get_posts_by_date(request,year,month,day):
    time=datetime.date(int(year),int(month),int(day))
    #current=datetime.date.today()
    #request.session["time"]=current
    paginator = Paginator(Entry.objects.filter(pub_date__year=time.year, pub_date__month=time.month, pub_date__day=time.day), 10)
    all_entry = Entry.objects.order_by('-pub_date')
    tags=Tag.objects.all()
    comment_list=Comment.objects.order_by('-date')
    
    links = Links.objects.all()
    try:
        page = int(request.GET.get('page', '1'))
        entry = paginator.page(page)
    except  InvalidPage:
        raise Http404

    return render_to_response("blog/main.html",{
                'paginator': paginator,#X
                'entry_list': entry,
                'all_entry_list': all_entry,
                'is_paginated': paginator.num_pages > 1,
                'has_next': paginator.page(page).has_next(),
                'has_previous': paginator.page(page).has_previous(),
                'current_page': page,
                'next_page': page + 1,
                'previous_page': page - 1,
                'pages': paginator.num_pages,
                #'hits' : paginator.hits,#X
                'page_numbers': range(paginator.num_pages+1)[1:],
                'comment_list': comment_list,
                'tags': tags,
                #'year': current.year,
                #'month': current.month,
                'link_list': links})     

def get_posts_by_tag(request,tagname):
    tag = Tag.objects.filter(title=tagname)[0]
    paginator = Paginator(tag.entry_set.all(), 10)
    all_entry = Entry.objects.order_by('-pub_date')
    tags=Tag.objects.all()
    comment_list=Comment.objects.order_by('-date')
    
    links = Links.objects.all()
    try:
        page = int(request.GET.get('page', '1'))
        entry = paginator.page(page)
    except  InvalidPage:
        raise Http404

    return render_to_response("blog/main.html",{
                'paginator': paginator,#X
                'entry_list': entry,
                'all_entry_list': all_entry,
                'is_paginated': paginator.num_pages > 1,
                'has_next': paginator.page(page).has_next(),
                'has_previous': paginator.page(page).has_previous(),
                'current_page': page,
                'next_page': page + 1,
                'previous_page': page - 1,
                'pages': paginator.num_pages,
               # 'hits' : paginator.hits,#X
                'page_numbers': range(paginator.num_pages+1)[1:],
                'comment_list': comment_list,
                'tags': tags,
                #'year': current.year,
                #'month': current.month,
                'link_list': links})     

def get_post(request, post_id=1):        
    try:        
        #current=datetime.date.today() 
        #request.session["time"]=current 
        tags=Tag.objects.all() 

        onepost = Entry.objects.get(id=post_id)
        count_entry = int(Entry.objects.count())
        current_id = int(post_id)
        if current_id > 1:
            pre_entry = Entry.objects.get(id=str(current_id-1))
        else:
            pre_entry = None
        if current_id < count_entry:
            next_entry = Entry.objects.get(id=str(current_id+1))
        else:
            next_entry = None
        comment_list = onepost.comment_set.all()
        
        rand_entry = []
        for e in Entry.objects.all():
            flag = random.randint(0, 1)
            if flag:
                rand_entry.append(e)
            
        return render_to_response("blog/post.html",
                {'entry':onepost,
                'pre_entry':pre_entry,
                'next_entry':next_entry,
                'rand_entry':rand_entry,
                'comment_list':comment_list,
                'tags':tags,
                #'year':current.year,
                #'month':current.month
                }) 
    
    except AssertionError, Entry.DoesNotExist:
        print ' ERROR in get_post' 
        return HttpResponseRedirect("/blog/")



#============================add by shenyan ==========================

def save_comment(request):
    comment_author=request.POST.get("name",None)
    comment_email=request.POST.get("email",None)
    comment_website=request.POST.get("homepage",None)
    comment_body=request.POST.get("content",None)
    comment_post_id=request.POST.get("postid",None)
    if not comment_author or not len(comment_author):
        if comment_post_id:
            return HttpResponseRedirect("/blog/post/"+comment_post_id+"/")
        else:
            return HttpResponseRedirect("/blog/")
    try:
        onepost=Entry.objects.get(id=comment_post_id)
        comment=Comment(author=comment_author, email=comment_email, website=comment_website, body=comment_body, date=datetime.datetime.now(),post=onepost)
        comment.save()
        return HttpResponseRedirect("/blog/post/"+comment_post_id+"#cmt_form")
        #return HttpResponseRedirect("/blog/")
    except Exception,e:
        return HttpResponse("Write Error")

# add by caijunjie 
# archiver
def get_archiver(request,time):#X
    current=datetime.date.today()
    request.session["time"]=current
    entry=Entry.objects.order_by('-pub_date')
                                                      
    tags=Tag.objects.all()
    comment_list=Comment.objects.all()
                                                      
    # add by caijunjie
    # 增加历史记录显示
    ################################################
    number_per_month={}
    for i in entry:
        if not number_per_month.has_key(str(i.pub_date)[0:7]):
            number_per_month[str(i.pub_date)[0:7]]=1
        else:
            number_per_month[str(i.pub_date)[0:7]]+=1
    
    year,month=time.split("-")
    entry=Entry.objects.filter(pub_date__year=int(year),pub_date__month=int(month))
    return render_to_response("blog/archiver.html",{"year":current.year,"month":current.month,"number_per_month":number_per_month,"tags":tags,"entry":entry})



# add by caijunjie
# category list

def list_category(request,cate):#X
    current=datetime.date.today()                                                         
    request.session["time"]=current
    entry=Entry.objects.order_by('-pub_date')
    tags=Tag.objects.all()
    comment_list=Comment.objects.all()
    # add by caijunjie
    # 增加历史记录显示
    ################################################

    number_per_month={}    
    for i in entry:
        if not number_per_month.has_key(str(i.pub_date)[0:7]):
            number_per_month[str(i.pub_date)[0:7]]=1
        else:
            number_per_month[str(i.pub_date)[0:7]]+=1
    
    
    tag=Tag.objects.get(title=cate)
    entry=Entry.objects.filter(tags=tag)
    #return render_to_response("blog/list.html",{'Entry':entry,'tags':tags})
    return object_list(request, entry, paginate_by=8, template_name='blog/list.html', extra_context={'tags':tags,'comment_list':comment_list,'year':current.year,'month':current.month,'number_per_month':number_per_month})


def search_blog(request):
    keywords = request.GET.get('keywords')
    if keywords:
        #query_string = r'^.*'+keywords+'.*$'
        paginator = Paginator(Entry.objects.filter(body__icontains=keywords), 10)
        all_entry = Entry.objects.order_by('-pub_date')
        tags=Tag.objects.all()
        comment_list=Comment.objects.order_by('-date')
        
        links = Links.objects.all()
        try:
            page = int(request.GET.get('page', '1'))
            entry = paginator.page(page)
        except  InvalidPage:
            raise Http404
        return render_to_response("blog/main.html",{
                'entry_list': entry,
                'all_entry_list': all_entry,#change to sidebar ??
                'is_paginated': paginator.num_pages > 1,
                'has_next': paginator.page(page).has_next(),
                'has_previous': paginator.page(page).has_previous(),
                'current_page': page,
                'next_page': page + 1,
                'previous_page': page - 1,
                'pages': paginator.num_pages,
                'page_numbers': range(paginator.num_pages+1)[1:],
                'comment_list': comment_list,#change to sidebar ??
                'tags': tags,
                'link_list': links,
                'search_keywords':keywords,})
    else:
        return HttpResponseRedirect("/blog/")
