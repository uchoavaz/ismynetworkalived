
from django.views.generic import TemplateView
from catcher.models import Network
from django.utils import timezone
from django.template import RequestContext
from django.shortcuts import render_to_response

def check_time(date_to_compare):
    time_now = timezone.now()
    seconds_difference = (timezone.localtime(time_now) - timezone.localtime(
        date_to_compare)).seconds

    if seconds_difference <= 230:
        return True

    return False

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        network_info = []
        context = super(HomeView, self).get_context_data(**kwargs)
        for network in Network.objects.all().distinct():
            status = check_time(network.last_datetime_connection)
            lista = [
                network.network_name, status, network.last_datetime_connection
            ]
            network_info.append(lista)

        context['network_info'] = network_info

        return context


def get_home(request):
    network_info = []
    for network in Network.objects.all().distinct():
        status = check_time(network.last_datetime_connection)
        lista = [
            network.network_name, status, network.last_datetime_connection
        ]
        network_info.append(lista)
    print (network_info)
    template = 'tr_body_home.html'
    return render_to_response(
        template,
        {'network_info': network_info},
        context_instance=RequestContext(request)
    )



home = HomeView.as_view()