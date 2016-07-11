from django.utils.translation import ugettext_lazy as _
from colab.plugins.utils.menu import colab_url_factory

name = 'colab_edemocracia'
verbose_name = 'Colab eDemocracia Plugin'

urls = {
    'include': 'colab_edemocracia.urls',
    'prefix': '^edem/',
    'namespace': 'colab_edemocracia',
}

dependencies = ['djangobower', 'compressor',]

settings_variables = {
    'STATICFILES_FINDERS': [
        'djangobower.finders.BowerFinder',
        'compressor.finders.CompressorFinder',
    ],
    'BOWER_COMPONENTS_ROOT': '/colab-plugins/edemocracia/src/colab_edemocracia/static',
    'BOWER_INSTALLED_APPS': (
        'foundation-sites',
    ),
    'COMPRESS_PRECOMPILERS': (
        ('text/x-scss', 'django_libsass.SassCompiler'),
    ),
    'COMPRESS_ROOT': '/colab-plugins/edemocracia/src/colab_edemocracia/static',
    'COLAB_TEMPLATES': ("/colab-plugins/edemocracia/src/colab_edemocracia/templates",),
    'COLAB_STATICS': ['/colab-plugins/edemocracia/src/colab_edemocracia/static']
}
