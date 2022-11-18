from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from accounts.views  import RegisterAPIView, UserDetail, LoginAPIView

urlpatterns = [
    path('api/userdetail', UserDetail.as_view({'get': 'list'}), name='userdetail'),
    path('api/login/', LoginAPIView.as_view(), name='login_view'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh_view'),
    path('api/register/', RegisterAPIView.as_view())
]