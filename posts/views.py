from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from posts.models import Post
from posts.serializers import PostSerializer
from scores.serializers import ScoreSerializer


class PostViewSet(
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(
        detail=True,
        methods=["post"],
        url_path="score",
        serializer_class=ScoreSerializer,
    )
    def create_score(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @action(
        detail=True,
        methods=["patch"],
        url_path="edit-score",
        serializer_class=ScoreSerializer,
    )
    def update_score(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
