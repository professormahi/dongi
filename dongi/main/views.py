from django.http import HttpResponse
from django.views import View


class HelloWorldView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        return HttpResponse("Hello World!")
