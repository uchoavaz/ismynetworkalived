
from django.views.generic import TemplateView
from django.http import HttpResponse
from .treat_request import treat_request


class CatcherView(TemplateView):
    def get(self, request, *args, **kwargs):

        request = self.request
        treat_request(request)
        return HttpResponse('')

catcher = CatcherView.as_view()
