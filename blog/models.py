from django.db import models 
from django.utils import timezone

from django.contrib import admin

#############
class Author(models.Model):
    name = models.CharField(max_length =50)
    age = models.IntegerField()
    def __unicode__(self):
         return self.name

# begin of adding by lsq
class AuthorAdmin(admin.ModelAdmin):
    list_display=('name','age')

admin.site.register(Author,AuthorAdmin)
# end of adding by lsq

#############
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    counter = models.IntegerField(default = 0)
    putDate = models.DateField(auto_now_add = True)
    author = models.ForeignKey(Author)
    def __unicode__(self):
         return self.title

# begin of adding by lsq
class BlogAdmin(admin.ModelAdmin):
    list_display=('id','title','content','counter','putDate','author')

admin.site.register(Blog,BlogAdmin)
# end of adding by lsq

#############
# begin of example  

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    timestamp = models.DateTimeField()

class BlogPostAdmin(admin.ModelAdmin):
    list_display=('title','content', 'timestamp')

admin.site.register(BlogPost,BlogPostAdmin)
# end of example
#############

