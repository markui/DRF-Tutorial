from django.conf.urls import url
from .views import snippet_list

app_name = 'snippets'

urlpatterns = [
    url(r'^$', snippet_list, name='list'),
]
