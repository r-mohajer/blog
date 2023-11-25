from rest_framework.routers import DefaultRouter

from posts.views import PostViewSet

app_name = "posts"
posts_router = DefaultRouter()
posts_router.register("", PostViewSet, basename="posts")

urlpatterns = posts_router.urls
