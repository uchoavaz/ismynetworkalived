from django.views.generic import TemplateView
from catcher.models import Network
from django.utils import timezone



class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        network_info = []
        context = super(HomeView, self).get_context_data(**kwargs)
        for network in Network.objects.all().distinct():
            status = self.check_time(network.last_datetime_connection)
            lista = [
                network.network_name, status, network.last_datetime_connection
            ]
            network_info.append(lista)

        context['network_info'] = network_info

        return context
    def check_time(self, date_to_compare):
        year_now = timezone.now().year
        year_to_compare = date_to_compare.year
        month_now = timezone.now().month
        month_to_compare = date_to_compare.month
        hours_now = timezone.now().hour
        hours_to_compare = date_to_compare.hour
        minutes_now = timezone.now().minute
        minutes_to_compare = date_to_compare.minute
        seconds_now = timezone.now().second
        seconds_to_compare = date_to_compare.second

        if year_to_compare == year_now and \
                month_to_compare == month_now and \
                hours_to_compare == hours_now and \
                minutes_to_compare == minutes_now \
                and (seconds_now - seconds_to_compare) <= 59:

                return True

        return False

home = HomeView.as_view()