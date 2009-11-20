#coding=utf-8
"""blog主数据库模型
@author:U{pprivulet<mailto:pprivulet@gmail.com>}
@license:MIT
@contact:pprivulet@gmail.com
"""
from django.db import models
from django.contrib.auth.models import User
from settings import MYIMAGE_DIR

# Create your models here.
class MUser(User):
    """用户类，继承原来的User包含属性.
    - username:用户名称
    - email:邮箱地址
    - password：密码
    - is_superuser:判断是否是特权用户
    - last_login：前一此登录
    - date_joined：加入时间
    - gender：用户性别
    - logo：用户头像
    """
    gender_choices = (
    	('M','Male'),
    	('F','Female'),
    )
    gender = models.CharField(max_length=1,choices=gender_choices)
    logo = models.ImageField(upload_to=MYIMAGE_DIR,)

class MTag(models.Model):
	'''标签类，用于分类文章。
	- name: 标题名称
	'''
	name = models.CharField(max_length=10,unique=True,
	help_text="指定标签的名字，不超过10个字符.")

class MPost(models.Model):    
	"""博文类，指示发表的文章。
	- title：文章标题
	- tag：文章类别标签
	- user：发文博主
	- content：文章内容 
	- createTime：发表时间	
	"""
	title = models.CharField(max_length=30,help_text="指定文章的标题，不超过30个字符.")
	tag = models.ManyToManyField(MTag)
	user = models.ForeignKey(MUser)
	content = models.TextField()
	createTime = models.DateTimeField()
	

class MComment(models.Model):   
	"""评论类，指示对文章进行评论.
	- post:评论的文章
	- user:发表评论的用户，缺省则是非注册用户
	- content:评论的内容
	- createTime:评论时间
	- email:发表评论的用户的邮件地址	
	""" 
	user = models.ForeignKey(MUser,null=True)
	post = models.ForeignKey(MPost)
	createDate = models.DateTimeField()
	content =  models.TextField()
	email = models.EmailField(max_length=50,null=True)
    
class MMessage(models.Model):
	"""消息类，指示对博客的留言.
	- user:留言的用户，缺省则为非注册用户
	- email:留言用户的邮件地址
	- content:留言内容  
	- createTime:留言时间  
	- checkTag:如是非注册用户则核查通过后显示留言		
	""" 
	user = models.ForeignKey(MUser,null=True)
	content = models.TextField()
	createTime = models.DateTimeField()
	checkTag = models.BooleanField()
	email = models.EmailField(max_length=50,null=True)
	
	
