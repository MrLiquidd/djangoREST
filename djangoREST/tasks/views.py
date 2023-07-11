import random

from rest_framework import viewsets, mixins, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Task, Category
from .serializers import TaskSerializer


class TaskViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        queryset = Task.objects.filter(category=pk)
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def first(self, request):
        queryset = Task.objects.all()[0:1]
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

