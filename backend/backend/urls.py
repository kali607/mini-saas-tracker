

from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from dashboard.views import SeverityChartView
# from .views import get_user_info
from django.http import JsonResponse 
from users.views import get_user_info
from users.auth_views import GoogleLogin  # Update 'your_app' to actual app name
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
schema_view = get_schema_view(openapi.Info(title="API", default_version="v1"), public=True)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

urlpatterns = [
    path('', lambda request: JsonResponse({"message": "Backend is running"})),
    path("admin/", admin.site.urls),
    path('api/', include('stats.urls')),
    path("api/auth/", include("dj_rest_auth.urls")),
    path("api/auth/registration/", include("dj_rest_auth.registration.urls")),
    path("api/auth/", include("allauth.socialaccount.urls")),
    path("api/docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("api/issues/", include("issues.urls")),
    path("api/dashboard/severity-chart/", SeverityChartView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/', include('allauth.urls')),
    path('api/auth/google/login/', GoogleLogin.as_view(), name='google_login'),
    path('user/', get_user_info, name='user-info'),
    path('api/user/', get_user_info),
    path('auth/google/', GoogleLogin.as_view(), name='google_login'),
    # path('accounts/', include('allauth.urls')),
    path('api/auth/google/', GoogleLogin.as_view(), name='google_login'),
    

]








