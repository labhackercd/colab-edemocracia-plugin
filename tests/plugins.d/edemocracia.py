from django.utils.translation import ugettext_lazy as _
from colab.plugins.utils.menu import colab_url_factory

name = 'colab_edemocracia'
verbose_name = 'Colab eDemocracia Plugin'

urls = {
    'include': 'colab_edemocracia.urls',
    'prefix': '',
    'namespace': 'colab_edemocracia',
}

dependencies = ['djangobower', 'compressor','easy_thumbnails',
                'image_cropping', 'widget_tweaks']

settings_variables = {
    'STATICFILES_FINDERS': [
        'djangobower.finders.BowerFinder',
        'compressor.finders.CompressorFinder',
    ],
    'BOWER_COMPONENTS_ROOT': '/vagrant_data/colab-edemocracia-plugin/src/colab_edemocracia/static',
    'BOWER_INSTALLED_APPS': (
        'foundation-sites',
        'jquery-mask-plugin',
        'https://github.com/labhackercd/fontastic-labhacker.git',
    ),
    'COMPRESS_PRECOMPILERS': (
        ('text/x-scss', 'django_libsass.SassCompiler'),
    ),
    'LIBSASS_SOURCEMAPS': 'DEBUG',
    'COMPRESS_ROOT': '/vagrant_data/colab-edemocracia-plugin/src/colab_edemocracia/static',
    'COLAB_TEMPLATES': ("/vagrant_data/colab-edemocracia-plugin/src/colab_edemocracia/templates",),
    'COLAB_STATICS': ['/vagrant_data/colab-edemocracia-plugin/src/colab_edemocracia/static']
}
