from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect,JsonResponse,FileResponse
from django.template import loader
from .models import Blog,BlogPost 

# simple :
def hello(request):
    return HttpResponse('<html> Hell World</html>')

# example :
def index(request):
    blog_list = BlogPost.objects.all()
    return render_to_response('index.html',{'blog_list':blog_list})

# more :
def showBlog(request,blogId):
	t = loader.get_template('blog.html')
	blog = Blog.objects.get(id=blogId)
	context = {'blog':blog}
	html = t.render(context)
	return HttpResponse(html)

# more :
def showBlogList(request):
	t = loader.get_template('blog_list.html')
	blogs=Blog.objects.all()
	context = {'blogs':blogs}
	html = t.render(context)
	return HttpResponse(html)

# more :
def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template('archive.html')
    c = {'posts':posts}
    return HttpResponse(t.render(c))
# 
    
