from rest_framework.routers import DefaultRouter
from post.api.views import PostApiViewSet

router_posts = DefaultRouter()
router_posts.register(prefix='posts', viewset=PostApiViewSet, basename='posts')