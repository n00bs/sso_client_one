from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from sso_client_one.views import HomeView, AuthenticateView

urlpatterns = [
    url(r'^token/', HomeView.as_view()),
    url(r'^authenticate/', AuthenticateView.as_view())
]
