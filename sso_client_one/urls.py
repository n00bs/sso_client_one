from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from sso_client_one.views import show_token

urlpatterns = [
    url(r'^token/', show_token.as_view()),
]
