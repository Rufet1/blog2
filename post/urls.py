from django.urls import path, re_path
from .views import * 
from django.conf.urls import url

app_name = "post"

urlpatterns = [
 path('index', post_index, name="index"),
 path('create', post_create, name="create"),
 url(r'^(?P<slug>[\w-]+)/$', post_detail, name="detail"),
 url(r'^(?P<slug>[\w-]+)/update/$', post_update, name="update"),
 url(r'^(?P<slug>[\w-]+)/delete/$', post_delete , name="delete"),
 url(r'^(?P<id>[\w-]+)/commentdelete/$', comment_delete , name="commentdelete"),

]