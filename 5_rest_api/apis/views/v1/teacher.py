from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from apis.serializers import TeacherSerializer
from apis.models import Teacher
from apis.filters import TeacherFilter

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TeacherFilter
