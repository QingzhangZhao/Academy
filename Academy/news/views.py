from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from news.models import *
from django.forms import ModelForm
# Create your views here.



class NewsForm( ModelForm ):
    class Meta:
        model = News
        fields = ['title','content','images']

def hello( request ):
    pass

def shownews( request,id):
    ctx = {}
    id = int(id)
    new = News.objects.get( id=id )
    for key in new.__dict__:
        if key.count('_') == 0:
            ctx[key] = new.__dict__[key]
    return JsonResponse(ctx)


# the add news is for admin in pc not for client
def addnews( request ):
    ctx = {}
    if request.method == 'POST':
        form = NewsForm( request.POST,request.FILES )
        if form.is_valid():
            try:
                image = request.FILES['images']
            except:
                image = None
            content = request.POST['content']
            title = request.POST['title']
            new_news = News(
                    images = image,
                    content = content,
                    title = title,
                    )
            new_news.save()
            return HttpResponseRedirect('/news/addnews/')
    else:
        form = NewsForm()
    ctx['form'] =  form
    return render_to_response('news.html',ctx)


def showall( request ):
    ctx = {}
    news = News.objects.all()
    for new in news:
        ctx[new.id] = new.title
    return JsonResponse(ctx)
