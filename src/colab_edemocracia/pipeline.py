from colab_edemocracia.models import UserProfile
from requests import request, HTTPError
from django.core.files.base import ContentFile


def save_profile(strategy, user, response, details, is_new=False, *args,
                 **kwargs):
    if kwargs['backend'].name == 'camara_deputados':
        profile, is_created = UserProfile.objects.get_or_create(user=user)
        url = response.get('foto')

        try:
            response_image = request('GET', url, verify=False)
            response_image.raise_for_status()
        except HTTPError:
            pass
        else:
            profile.avatar.save('{0}_social.jpg'.format(user.username),
                                ContentFile(response_image.content))
        profile.uf = response.get('uf')
        profile.gender = response.get('sexo')
        profile.country = response.get('pais')
        profile.birthdate = response.get('dataNascimento')

        profile.save()
