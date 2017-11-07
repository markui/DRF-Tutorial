from django.conf.urls import url

from ..views.cbv_mixins import SnippetList, SnippetDetail

urlpatterns = [
    url(r'^$', SnippetList.as_view(), name='snippet_list'),
    url(r'^(?P<pk>\d+)/$', SnippetDetail.as_view(), name='snippet_detail')
]
