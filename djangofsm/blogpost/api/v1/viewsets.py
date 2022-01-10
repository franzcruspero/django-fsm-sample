from datetime import datetime

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response


from blogpost.api.v1.serializers import BlogPostSerializer
from blogpost.models import BlogPost


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    STATE_NEW = "new"
    STATE_PENDING = "pending"
    STATE_PUBLISHED = "published"
    STATE_DESTORYED = "destroyed"

    @action(detail=True, methods=["post"])
    def publish(self, request, pk):
        instance = self.get_object()
        instance.publish()
        instance.save()

        return Response({}, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"])
    def unpublish(self, request, pk):
        instance = self.get_object()
        instance.destroy()
        instance.save()

        return Response({}, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"])
    def pending(self, request, pk):
        instance = self.get_object()
        instance.pending(is_moderator=True)
        instance.save()

        return Response({}, status=status.HTTP_200_OK)
