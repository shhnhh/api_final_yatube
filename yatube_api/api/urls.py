from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import (
    CommentViewSet,
    PostViewSet,
    GroupViewSet,
    FollowViewSet
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')
router.register(r'follow', FollowViewSet)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token,
         name='api_token'),
    path('v1/jwt/create/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/jwt/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('v1/jwt/verify/', TokenVerifyView.as_view(),
         name='token_verify'),
    path('v1/', include(router.urls)),
]
