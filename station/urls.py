from django.urls import path, include
from .views import index, automation, run_automation

urlpatterns = [
    path(route="", view=index, name="index"),
    path(route="automation/", view=automation, name="automation"),
    path(
        route="run_automation/<str:id>",
        view=run_automation,
        name="run_automation",
    ),
]
