from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from ..views.fbv import *

app_name = 'snippets'

urlpatterns = [
    url(r'^$', snippet_list, name='list'),
    url(r'^(?P<pk>\d+)/$', snippet_detail, name='detail'),
]
# urlpatterns = format_suffix_patterns(urlpatterns)
