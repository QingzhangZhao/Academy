from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from news.models import *
from django.forms import ModelForm
# Create your views here.

LASTID = 1

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
            global LASTID
            LASTID = new_news.id
            print(LASTID)
            return HttpResponseRedirect('/news/showall/')
    else:
        form = NewsForm()
    ctx['form'] =  form
    return render_to_response('news.html',ctx)

def showall( request ):
    ctx = {}
    try:
        pStart = int(request.GET['page'])
    except:
        pStart = 0
    tStart = 10*pStart
    news = News.objects.all()[tStart:(tStart+10)]
    ctx['news'] = news
    ctx['pre'] = (0 if pStart==0 else pStart-1)
    ctx['next'] = ( pStart if news.count()<10 else pStart+1 )
    return render_to_response('showall.html',ctx)

def delnews( request,id ):
    id = int(id)
    the_new = News.objects.filter( id=id )
    if the_new:
        the_new = the_new[0].delete()
    return HttpResponseRedirect('/news/showall/')

def editnews( request,id ):
    id = int(id)
    ctx = {}
    the_news = News.objects.get( id=id )
    if request.method == 'POST':
        form = NewsForm( request.POST,request.FILES )
        if form.is_valid():
            try:
                image = request.FILES['images']
            except:
                image = None
            the_news.title = request.POST['title']
            the_news.content = request.POST['content']
            the_news.save()
            return HttpResponseRedirect('/news/showall/')
        ctx['form'] = form
    ctx['news'] = the_news
    return render_to_response('edit.html',ctx)

def all( request ):
    ctx = {}
    global LASTID
    if LASTID == 1:
        LASTID = News.objects.order_by('-id')[0].id
    ctx['ID'] = LASTID
    return JsonResponse(ctx)
