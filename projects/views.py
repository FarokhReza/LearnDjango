from os import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project, Tag
from .forms import ProjectForm, ReviewForm
from .utils import searchProjects, paginateProjects
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
    projects, search_query = searchProjects(request)

    custom_range, projects = paginateProjects(request, projects, 3)

    context = { 'projects': projects, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'projects/projects.html', context)  # will go in setting.py find dir template and use from 
        # content


def project(request, pk):
    # return HttpResponse('SINGLE PROJECT' + ' ' + str(pk))
    projectObj = Project.objects.get(id=pk)
    # tags = projectObj.tags.all()
    # print('projectObj:', projectObj)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()

        projectObj.getVoteCount

        #upadte project votecount
        messages.success(request, "Your review submitted")
        return redirect('project', pk=projectObj.id)
    
    context = {'project': projectObj, 'form': form}

    return render(request, 'projects/single-project.html', context)

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', ' ').split()
        # form = ProjectForm(request.POST, request.FILES)
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()

            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
                
            return redirect ('account')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)

@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    # project = Project.objects.get(id=pk)
    project = profile.project_set.get(id=pk)  # now only the project owner can update project
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', ' ').split()
        # form = ProjectForm(request.POST, request.FILES, instance=project)
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)

            return redirect ('account')

    context = {'form': form, 'project': project}
    return render(request, "projects/project_form.html", context)

@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    # project = Project.objects.get(id=pk)
    project = profile.project_set.get(id=pk)  # now only the project owner can delete project
    if request.method == 'POST':
        project.delete()
        # return redirect ('account')
        return redirect ('projects')
    context = {'object': project}
    return render(request, 'delete_template.html', context)