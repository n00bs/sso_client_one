from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.urls import reverse
from django.shortcuts import redirect, render_to_response
from django.conf import settings
from django.views import View
from django.template import RequestContext, loader


# inheriting from API VIEW is all that is required for DRF auth
class HomeView(APIView):
    template_name = "token.html"

    def get(self, request, *args, **kwargs):
        context = {}
        if request.user.is_authenticated:
            reply = "I know you! You are %s." % request.user
        else:
            token_URL = AuthenticateView().token_URL("/client/token/")
            reply = "I don't know you. You are not logged in."
            context["token_URL"] = token_URL
        context["reply"] = reply
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))


class AuthenticateView(APIView):
    def get(self, request, format=None):
        token = self.request.GET.get('token', None)
        return_to = self.request.GET.get('return_to', None)
        if return_to is None:
            response = Response("return_to param missing.")
        elif token is None:
            response = Response("token missing.")
        else:
            response = redirect(return_to + "?token=" + token)
        return response

    def token_URL(self, return_to=None):
        sso_URL = settings.SSO_URL
        login_URL = settings.LOGIN_URL
        token_URL = sso_URL + "?login_at=" + login_URL
        if return_to is not None:
            token_URL += "&return_to=" + return_to
        return token_URL
