# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from google.appengine.ext import db
from django.contrib.auth.models import User

class UserInfo(db.Model):
    owner = db.ReferenceProperty(User)                  # 谁的信息
    website = db.LinkProperty()                         # 网站
    avatar = db.BlobProperty()                          # 头像
    date = db.DateTimeProperty(auto_now_add=True)
    checkNotify = db.BooleanProperty()                  # 是否有新的通知
    
    def __str__(self):
        return "%s's info" % self.owner.nickname()
    
    def __unicode__(self):
        return u"%s's info" % self.owner.nickname()
        
    
class Tag(db.Model):
    title = db.StringProperty()                         # 标签名称
    date = db.DateTimeProperty(auto_now_add=True)       # 创建日期
    isPost = db.BooleanProperty()                       # True是文章标签, False为图片标签
    date = db.DateTimeProperty(auto_now_add=True)
    
    def get_url(self):
        return '/tag/%s/' % self.title
    
    def __str__(self):
        return '%s' % self.title
    
    def __unicode__(self):
        return u'%s' % self.title

class Photo(db.Model):
    owner = db.ReferenceProperty(User)              # 上传者
    description = db.TextProperty()                 # 图片描述
    body = db.BlobProperty()                        # 图片实体
    date = db.DateTimeProperty(auto_now_add=True)   # 创建日期
    tags = db.ListProperty(db.Category)             # 标签
    
    def get_url(self, f=False):
        return "/image/%s/" % self.key().id()
    
    def get_thu_url(self, f=False):
        return "/thumb/%s/" % self.key().id()
    
    def __str__(self):
        return '%s' % self.description
    
    def __unicode__(self):
        return u'%s' % self.description
    

class Entry(db.Model):
    author = db.ReferenceProperty(User)             # 作者
    title = db.StringProperty()                     # 标题
    content = db.TextProperty()                     # 内容
    date = db.DateTimeProperty(auto_now_add=True)   # 日期
    tags = db.ListProperty(db.Category)             # 标签
    clicknumber = db.IntegerProperty()              # 点击次数
    slug = db.StringProperty()                      # url简短字串
    
    def get_url(self):
        return '/post/%s/' % self.key().id()
    
    def __str__(self):
        return '%s' % self.title
    
    def __unicode__(self):
        return u'%s' % self.title

class Comment(db.Model):
    entry = db.ReferenceProperty(Entry)             # 哪个Entry
    cmt = db.SelfReferenceProperty()                # 哪个Comment, 如果两者都无, 表示留言信息
    author = db.UserProperty()                      # 评论者
    body = db.TextProperty()                        # 内容
    date = db.DateTimeProperty(auto_now_add=True)
    
    def get_title(self):
        if self.post:
            return 'Comment To: %s' % self.post.get_title()
        elif self.cmt:
            return 'Comment To: %s' % self.cmt.author.nickname()
        return "Message %s" % self.key().id()
    
    def get_url(self):
        if self.entry or self.cmt:
            return '/comment/%s/' % self.key().id()
        return '/comment/%s/' % self.key().id()
    
    def get_show_url(self):
        if self.entry or self.cmt:
            return "%s#cmt-%s" % (self.entry.get_url(), self.key().id())
        return '/comment/%s/' % self.key().id()
    
    def __str__(self):
        return '%s' % self.body
    
    def __unicode__(self):
        return u'%s' % self.body
    

class Links(db.Model):
    name = db.StringProperty()                      # 链接所属
    website = db.LinkProperty()                     # 链接地址
    description = db.StringProperty()               # 描述
    date = db.DateTimeProperty(auto_now_add=True)
    
    def __str__(self):
        return '%s' % self.website

    def __unicode__(self):
        return u'%s' % self.website
    


