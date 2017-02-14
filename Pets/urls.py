from django.conf.urls import url
from Pets import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^publish/$', views.publish, name='index'),
]