from django.conf.urls import include,url

urlpatterns = [
        url(r'^show/$','news.views.hello'),
        ]
