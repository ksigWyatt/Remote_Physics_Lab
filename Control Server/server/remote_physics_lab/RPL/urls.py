from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from RPL import views

urlpatterns = [
    url(r'^rpl/$', views.RplList.as_view(), name='rpl-list'),
    url(r'^rpl/(?P<pk>[0-9]+)/$', views.RplDetail.as_view(), name='rpl-detail'),
    # url(r'^$', views.index, name='index'),
]