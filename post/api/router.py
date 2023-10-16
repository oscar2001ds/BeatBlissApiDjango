from rest_framework.routers import DefaultRouter
from post.api.views import PostApiViewSet, SongFilesApiViewSet, AlbumApiViewSet, ArtistApiViewSet, GenreApiViewSet, UserApiViewSet

router_posts = DefaultRouter()
router_posts.register(prefix='posts', viewset=PostApiViewSet, basename='posts')
router_posts.register(prefix='songfiles', viewset=SongFilesApiViewSet, basename='songfiles')
router_posts.register(prefix='albums', viewset=AlbumApiViewSet, basename='albums')
router_posts.register(prefix='artists', viewset=ArtistApiViewSet, basename='artists')
router_posts.register(prefix='genres', viewset=GenreApiViewSet, basename='genres')
router_posts.register(prefix='users', viewset=UserApiViewSet, basename='users')
