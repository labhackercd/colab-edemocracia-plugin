
from django.conf.urls import patterns, url

from .views import ColabEdemocraciaProxyView

urlpatterns = patterns('',
    url(r'^(?P<path>.*)$', ColabEdemocraciaProxyView.as_view(),
        name='colab_edemocracia'),
)
