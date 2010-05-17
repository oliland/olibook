from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', "stream.views.stream", name="stream"),
)
