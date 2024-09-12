from rest_framework.routers import SimpleRouter
from django.urls import include, path

from api.views import (PostViewSetAndDetail,
                       CommentViewSetAndDetail,
                       GroupViewSet,
                       FollowViewSet)

router_v1 = SimpleRouter()
router_v1.register('posts', PostViewSetAndDetail, basename='post')
router_v1.register(r'posts/(?P<post_pk>\d+)/comments',
                   CommentViewSetAndDetail,
                   basename='comment')
router_v1.register('groups', GroupViewSet)
router_v1.register('follow', FollowViewSet, basename='follow')

urlpatterns = [path('', include(router_v1.urls)), ]
