from django.shortcuts import render,render_to_response
from django.http import HttpResponse
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
    id = int(id)
    pass


# the add news is for admin in pc not for client
def addnews( request ):
    ctx = {}
    if request.method == 'POST':
        form = NewsForm( request.POST,request.FILES )
        if form.is_valid():
            try:
                image = request.FILES['image']
            except:
                image = None
            content = request.POST['content']
            title = request.POST['title']
            new_news = News(
                    images = images,
                    cotent = content,
                    title = title,
                    cNum = 0,
                    view = 1
                    )
            new_news.save()]
            return HttpResponseRedirect('/news/addnews/')
    else:
        form = NewsForm()
    ctx['form'] =  form
    return render_to_response('news.html',ctx)

def addcomment( request,id ):
    id = int(id)
    pass
