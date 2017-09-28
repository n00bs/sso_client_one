from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.urls import reverse


class ExampleView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        if request.user.is_authenticated:
            print "example"
            return Response("example view")
        else:
            return Response("not logged in")
            # import pdb; pdb.set_trace()
            #return HttpResponseRedirect(
            #    "http://localhost:8003/sso/authorize/?successful_redirect_url=http://localhost:8002/client/token/"
            #)
