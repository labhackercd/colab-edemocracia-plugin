from social.backends.oauth import BaseOAuth2
from django.conf import settings


class CamaraOAuth2(BaseOAuth2):
    name = 'camara_deputados'
    AUTHORIZATION_URL = settings.CAMARA_DEPUTADOS_AUTHORIZATION_URL
    ACCESS_TOKEN_URL = settings.CAMARA_DEPUTADOS_ACCESS_TOKEN_URL
    METADATA_URL = settings.CAMARA_DEPUTADOS_METADATA_URL

    def get_user_details(self, response):
        return {'email': response.get('email'),
                'first_name': response.get('name')}

    def user_data(self, access_token, *args, **kwargs):
        return self.get_json(self.METADATA_URL, headers={
            'Authorization': 'Bearer %s' % access_token
        })
