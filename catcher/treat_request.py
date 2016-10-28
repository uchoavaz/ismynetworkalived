
from ipware.ip import get_ip
from .models import Network


def treat_request(request):
    ip = get_ip(request)
    name = request.GET.get('network_name')

    try:
        Network.objects.filter(network_name=name).delete()
    except:
        pass
    try:
        Network.objects.create(
            network_name=name,
            ip=ip
        )
    except:
        pass
