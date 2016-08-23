from colab_wikilegis.models import WikilegisBill
from colab_discourse.models import DiscourseTopic
from colab.plugins.data import PluginDataImporter


class ColabEdemocraciaDataImporter(PluginDataImporter):
    app_label = 'colab_edemocracia'

    def fetch_data(self):
        pass


def get_home_data():
    wikilegis_data = WikilegisBill.objects.all().order_by('-modified')
    discourse_data = DiscourseTopic.objects.all().order_by('-last_posted_at')
    return {'wikilegis_data': wikilegis_data, 'discourse_data': discourse_data}
