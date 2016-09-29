from django import template
from colab_discourse.models import DiscourseCategory
register = template.Library()


@register.assignment_tag(takes_context=True)
def get_prefered_themes_list(context):
    request = context['request']
    if not request.user.is_authenticated():
        return []
    return request.user.profile.prefered_themes.all().values_list('slug',
                                                                  flat=True)


@register.assignment_tag(takes_context=True)
def get_select_all_info(context):
    request = context['request']
    if not request.user.is_authenticated():
        return ''

    profile_categories = list(request.user.profile.prefered_themes.all())
    user_has_all_categories = True
    for category in DiscourseCategory.objects.all():
        if category not in profile_categories:
            user_has_all_categories = False

    select_all_info = {}
    select_all_info['class'] = 'deselect' if user_has_all_categories else ''
    if user_has_all_categories:
        select_all_info['text'] = 'Deselecionar todos'
    else:
        select_all_info['text'] = 'Selecionar todos'

    return select_all_info
