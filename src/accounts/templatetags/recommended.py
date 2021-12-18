from django import template

from accounts.models import Profile, User

register = template.Library()


@register.inclusion_tag("accounts/snippets/recommend.html")
def recommended(user):
    if isinstance(user, User):
        qs = Profile.objects.recommended(user)
        return {"recommended": qs}
