import json
import time
from django.shortcuts import render
from django.conf import settings
from django.template.defaultfilters import Context
import requests
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
    return render(request, "automation.html", context)


def run_automation(request, id):
    workflow = repo.get_workflow(id)
    status = workflow.create_dispatch(ref="main")
    if status == True:
        time.sleep(5)
        last_run = list(repo.get_workflow_runs())[0]
        run_url = repo.get_workflow_run(last_run.id).html_url
        context = {"workflow": workflow.name, "workflow_url": run_url}
        return render(request, "run_automation.html", context)
    else:
        context = {"detail": "Workflow dispatch failed"}
        return render(request, "run_automation.html", context)


# def automation_detail(request, id):
#     workflow_run_logs = []
#     workflow = repo.get_workflow(id)
#     # status = workflow.create_dispatch(ref="main")
#     last_run = list(repo.get_workflow_runs())[-1]
#     workflow_job = requests.get(
#         last_run.jobs_url,
#         headers={
#             "Accept": "application/vnd.github+json",
#             "Authorization": f"Bearer {settings.GITHUB_TOKEN}",
#             "X-GitHub-Api-Version": "2022-11-28",
#         },
#     )

#     for job in json.dumps(workflow_job.content)["jobs"]:
#         workflow_run_logs.append({job["name"]: job["steps"]})

#     context = {"workflow": workflow.name, "workflow_logs": workflow_run_logs}
#     return render(request, "automation_detail.html", context)
