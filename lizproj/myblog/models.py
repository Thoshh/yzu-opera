from django.db import models

# Create your models here.
#class User(models.Model):#X
#    GENDER_CHOICES=(
#    ('M', 'Male'),
#    ('F', 'Female'),
#    )
#    gender=models.CharField(maxlength=1, choices=GENDER_CHOICES)

#    name=models.CharField(maxlength=20)
#    passwd=models.CharField(maxlength=20)
    
#    def __str__(self):
#        return self.name    
#    class  Admin:
#        list_display = ('name', 'gender',)
#        search_fields = ('name',)        
    
class Tag(models.Model):
    slug=models.SlugField(prepopulate_from=('title',), primary_key=True)
    title=models.CharField(maxlength=30)
    description=models.TextField(help_text='Short summary of this tag')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/blog/tag/%s/" % self.title
    
    class Admin:
        list_display = ('slug', 'title',)
        search_fields = ('title', 'description',)
    
    class Meta:
        ordering = ('title',)

class Entry(models.Model):
    title=models.CharField(maxlength=200)
    body=models.TextField()
    pub_date=models.DateTimeField()

    tags = models.ManyToManyField(Tag)
    
    class Meta:
        get_latest_by = 'pub_date'

    class Admin:
        list_display = ('pub_date', 'title')
        search_fields = ['title','body']
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/blog/post/%i/" % self.id

class Comment(models.Model):
    post = models.ForeignKey(Entry)

    author = models.CharField(maxlength=64)
    email  = models.EmailField()
    website = models.CharField(maxlength=128)
                        
    body = models.TextField(null=True)
    date = models.DateTimeField()
    order = models.IntegerField(default=0)
                                     
    class Meta:
        ordering = ('order', )

    class Admin:
        list_display = ('post', 'author', 'email', 'website', 'date', 'order', 'body')
                                                                        
        def __repr__(self):
            return self.body
    
    def get_absolute_url(self):
        return "/blog/post/%i#cmt_form" % self.post.id    

class Links(models.Model):
    name = models.CharField(maxlength=64)
    #website = models.CharField(maxlength=128)
    website = models.URLField()
    description = models.CharField(maxlength=128)
    class Admin:
        list_display = ('name', 'website', 'description')
