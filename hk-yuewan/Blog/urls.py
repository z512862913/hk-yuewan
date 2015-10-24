from django.conf.urls import url
urlpatterns = [
    url(r'^register/$','Blog.views.register'),
    url(r'^login/$','Blog.views.login'),
    url(r'^login/register/$','Blog.views.register'),
    url(r'^changepassword/(?P<username>.*)/$','Blog.views.changepassword'),
    url(r'^$','Blog.views.index'),
    url(r'^post/(?P<uname>.*)/$','Blog.views.post'),
    url(r'^detail/(\d+)/$','Blog.views.detail'),
    url(r'^logout/$','Blog.views.logout'),
    url(r'^delete/(?P<post_id>\d+)/(?P<uname>.*)/$','Blog.views.delete'),
    url(r'^edit/(?P<post_id>\d+)/(?P<uname>.*)/$','Blog.views.edit'),
    url(r'^join/(?P<post_id>\d+)/(?P<uname>.*)/$','Blog.views.join'),
]
