from django.contrib.auth import get_user_model
from rest_framework_sso import claims
from django.http import HttpResponse
from rest_framework.views import APIView


class show_token(APIView):
    def get_context_data(self, **kwargs):
        print "logged"
        return HttpResponse("logged in")
