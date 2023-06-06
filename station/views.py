from django.shortcuts import render
from django.conf import settings
from django.template.defaultfilters import Context
from hcloud import Client


def index(request):
    hc_client = Client(token=settings.HCLOUD_TOKEN)
    servers = hc_client.servers.get_all()
    context = {"servers": servers}
    return render(request, "index.html", context)
