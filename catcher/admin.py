from django.contrib import admin
from .models import Network


class NetworkAdmin(admin.ModelAdmin):
    search_fields = [
        'network_name', 'ip', 'last_datetime_connection'
    ]
    list_display = (
        'network_name', 'ip', 'last_datetime_connection'
    )

admin.site.register(Network, NetworkAdmin)