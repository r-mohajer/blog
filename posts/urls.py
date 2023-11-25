from rest_framework.routers import DefaultRouter

from posts.views import PostViewSet

app_name = "posts"
posts_router = DefaultRouter()
posts_router.register("calendars", PostViewSet, basename="calendars")

urlpatterns = posts_router.urls
