from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from sso_client_one.views import ExampleView
from django.views.generic import TemplateView


urlpatterns = [
    # url(r'^token/', TemplateView.as_view(template_name="token.html")),
    url(r'^token/', ExampleView.as_view())
]
