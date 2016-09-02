from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect,JsonResponse,FileResponse
from django.template import loader
from .models import blog

# 

def showBlog(request,blogId):
	t = loader.get.template('blog.html')
	blog = Blog.objects.get(id=blogId)
	context = {'blog':blog}
	html = t.render(context)
	return HttpResponse(html)

def showBlogList(request):
	t = loader.get_template('blog_list.html')
	blogs=Blog.objects.all()
	context = {'blogs':blogs}
	html = t.render(context)
	return HttpResponse(html)


