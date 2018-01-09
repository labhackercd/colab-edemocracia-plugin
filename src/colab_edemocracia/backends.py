from social.backends.oauth import BaseOAuth2
from django.conf import settings
from colab_edemocracia.views import generate_username


class CamaraOAuth2(BaseOAuth2):
    name = 'camara_deputados'
    AUTHORIZATION_URL = settings.CAMARA_DEPUTADOS_AUTHORIZATION_URL
    ACCESS_TOKEN_URL = settings.CAMARA_DEPUTADOS_ACCESS_TOKEN_URL
    METADATA_URL = settings.CAMARA_DEPUTADOS_METADATA_URL
    ACCESS_TOKEN_METHOD = 'POST'
    DEFAULT_SCOPE = ['openid']

    def get_user_details(self, response):
        return {'username': generate_username(response.get('email')),
                'email': response.get('email'),
                'first_name': response.get('nome')}

    def user_data(self, access_token, *args, **kwargs):
        return self.get_json(self.METADATA_URL, headers={
            'Authorization': 'Bearer %s' % access_token
        })

    def auth_complete_credentials(self):
        return self.get_key_and_secret()
