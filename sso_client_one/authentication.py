from django.contrib.auth import get_user_model
from rest_framework_sso import claims


def authenticate_payload(payload):
    user_model = get_user_model()
    user, created = user_model.objects.get_or_create(
        username=payload.get(claims.USER_ID),
    )
    if not user.is_active:
        raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))
    if not created:
        raise exceptions.AuthenticationFailed(_('Error occured while creating \
        account on this service.'))
    return user
