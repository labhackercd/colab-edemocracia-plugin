
from django.utils.translation import ugettext_lazy as _
from colab.plugins.utils.menu import colab_url_factory

name = 'colab_edemocracia'
verbose_name = 'Colab Edemocracia Plugin'

#upstream = 'localhost'
# middlewares = []

#urls = {
#    'include': 'colab_edemocracia.urls',
#    'prefix': '^colab_edemocracia/',
#}

menu_title = _('colab_edemocracia')

url = colab_url_factory('colab_edemocracia')

# Extra data to be exposed to plugin app config
extra = {}

menu_urls = (
# Example of menu URL:
    url(display=_('Public Projects'), viewname='colab_edemocracia',
        kwargs={'path': 'public/projects'}, auth=False),

# Example of authenticated user menu URL:
#    url(display=_('Profile'), viewname='colab_edemocracia',
#        kwargs={'path': 'profile'}, auth=True),
)
