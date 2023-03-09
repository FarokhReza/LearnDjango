from django.shortcuts import render
from django.http import HttpResponse


projectList = [
    {
    'id' : '1',
    'title' : 'Ecommerce Website',
    'description' : 'this is about a mobile app'
    },

    {
    'id' : '2',
    'title' : 'Protfolio',
    'description' : 'this is about backend'
    },
    {
    'id' : '3',
    'title' : 'Mumble social network',
    'description' : 'this is about game'
    }
]


def projects(request):
    # return HttpResponse('Here are our products')
    page = 'projects'
    number = 10
    context = {'page': page, 'number': number, 'projects': projectList}
    return render(request, 'projects/projects.html', context)  # will go in setting.py find dir template and use from 
        # content


def project(request, pk):
    # return HttpResponse('SINGLE PROJECT' + ' ' + str(pk))
    projectObj = None
    for i in projectList:
        if i["id"] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})