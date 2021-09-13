from rest_framework import generics, viewsets

from project.api.serializers import ProjectSerializer
from project.models import Project


class ProjectAPIView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ProjectViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    # lookup_value_regex = '[0-9a-f]{32}'
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer




