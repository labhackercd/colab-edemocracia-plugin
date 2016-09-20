from django import template
register = template.Library()


@register.assignment_tag(takes_context=True)
def get_prefered_themes_list(context):
    request = context['request']
    if not request.user.is_authenticated():
        return []
    return request.user.profile.prefered_themes.all().values_list('slug',
                                                                  flat=True)
