from django.conf.urls import include,url
from django.conf.urls import patterns 

urlpatterns = patterns('news.views',
        (r'^all/$','all'),
        (r'showall/$','showall'),
        (r'delnews/(?P<id>\d+)/$','delnews'),
        (r'editnews/(?P<id>\d+)/$','editnews'),
        (r'^show/(\d+)/$','shownews'),
        #(r'^comment/(?P<id>\d+)/$','showcomments'),#id is the news's id
        (r'^addnews/$','addnews'),
        #(r'^addcomment/(?P<id>\d+)/','addcomment'),
        )
