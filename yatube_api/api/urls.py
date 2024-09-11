from rest_framework.routers import SimpleRouter
from django.urls import include, path

from api.views import (PostViewSetAndDetail,
                       CommentViewSetAndDetail,
                       GroupViewSet,
                       FollowViewSet)

router = SimpleRouter()
router.register('posts', PostViewSetAndDetail, basename='post')
router.register(r'posts/(?P<post_pk>\d+)/comments',
                CommentViewSetAndDetail,
                basename='comment')
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [path('', include(router.urls)), ]
