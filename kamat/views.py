from django.shortcuts import render

from kamat.models import Project

# Create your views here.

def project_index(request):
    kamat = Project.objects.all()
    context = {
        'kamat': kamat
    }
    return render(request, 'project_index.html', context)
	
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)