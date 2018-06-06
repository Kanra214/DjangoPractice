
from django.conf.urls import url, include
from . import views
# Create your views here.
urlpatterns = [
	
	#/appxiyun/
    url(r'^$', views.index, name = 'index'),

    #/appxiyun/712/
    url(r'^/(?P<album_id>[0-9]+)$', views.detail, name = 'detail'),
]