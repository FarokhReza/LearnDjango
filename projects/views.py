from django.shortcuts import render
from django.http import HttpResponse


def projects(request):
    # return HttpResponse('Here are our products')
    return render(request, 'projects/projects.html')  # will go in setting.py find dir template and use from 
        # content


def project(request, pk):
    # return HttpResponse('SINGLE PROJECT' + ' ' + str(pk))
    return render(request, 'projects/single-project.html')

