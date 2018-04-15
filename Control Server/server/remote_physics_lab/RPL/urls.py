from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from RPL import views
from .views import update_value

urlpatterns = [
    url(r'^rpl/$', views.RplList.as_view(), name='rpl-list'),
    url(r'^$', update_value, name='update')
]