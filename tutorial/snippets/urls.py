from django.conf.urls import url
from .views import snippet_list, snippet_detail

app_name = 'snippets'

urlpatterns = [
    url(r'^$', snippet_list, name='list'),
    url(r'^(?P<pk>\d+)/$', snippet_detail, name='detail'),
]
