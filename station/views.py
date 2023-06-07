from django.shortcuts import render
from django.conf import settings
from django.template.defaultfilters import Context
from hcloud import Client
from github import Github


g = Github(settings.GITHUB_TOKEN)
repo = g.get_repo("khushmeeet/infra")


def index(request):
    hc_client = Client(token=settings.HCLOUD_TOKEN)
    servers = hc_client.servers.get_all()
    context = {"servers": servers}
    return render(request, "index.html", context)


def automation(request):
    workflows = repo.get_workflows()
    context = {"workflows": list(workflows)}
    print(context)
    return render(request, "automation.html", context)


def run_automation(request, id):
    workflow = repo.get_workflow(id)
    status = workflow.create_dispatch(ref="main")
    if status == True:
        last_run = list(repo.get_workflow_runs())[-1]
        last_run._requester.requestJson("GET", last_run.logs_url)
    context = {"workflow": workflow.name}
    return render(request, "run_automation.html", context)
