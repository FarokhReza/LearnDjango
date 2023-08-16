from django.http import JsonResponse
from projects.views import project
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Project, Review, Tag

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET': '/api/projects'},
        {'GET': '/api/projects/id'},
        {'POST': '/api/projects/id/vote'},

        {'POST': '/api/users/toket'},
        {'POST': '/api/users/toket/refresh'},
    ]

    return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])  # any time user want get project from here it shoulde be
# Authenticated
def getProjects(request):
    print('USER:', request.user)
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProject(request, pk):
    projects = Project.objects.get(id=pk)
    serializer = ProjectSerializer(projects, many=False)
    
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request, pk):
    project = Project.objects.get(id=pk)
    user = request.user.profile
    data = request.data # becaouse of decorator we can run this
    review, created = Review.objects.get_or_create(
        owner=user,
        project=project,
    )
    
    review.value = data['value']
    review.save()
    project.getVoteCount
    serializer = ProjectSerializer(project, many=False)
    
    return Response(serializer.data)

# @api_view(['DELETE'])
# def removeTag(request):
#     tagId = request.data['tag']
#     projectId = request.data['project']

#     project = Project.objects.get(id=projectId)
#     tag = Tag.objects.get(id=tagId)

#     project.tags.remove(tag)


#     return Response('Tag was deleted!')


# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Project, Tag

@api_view(['DELETE'])
def removeTag(request):
    tagId = request.data.get('tag')  # Use .get() to avoid KeyError
    projectId = request.data.get('project')  # Use .get() to avoid KeyError

    if tagId is not None and projectId is not None:
        try:
            project = Project.objects.get(id=projectId)
            tag = Tag.objects.get(id=tagId)
            project.tags.remove(tag)
            return Response('Tag was deleted!')
        except (Project.DoesNotExist, Tag.DoesNotExist):
            return Response('Project or Tag does not exist.', status=400)

    return Response('Missing tag or project key in request data.', status=400)
