from django.urls import path, include
from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.decorators.csrf import csrf_exempt

from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# from .views import LoginAPIView
# from .views import LoginAPIView

router = routers.DefaultRouter()
router.register(r'subjects', views.SubjectsViewSet)
router.register(r'chapters', views.ChaptersViewSet)
router.register(r'themes', views.QuestionThemeViewSet)
router.register(r'questions', views.QuestionViewSet)


schema_view = get_schema_view(
   openapi.Info(
      title="Test Manager API",
      default_version='v1',
      description="Test API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
# path('register/',  csrf_exempt(RegisterAPIView.as_view()), name='register'),
    # path('login/get_token/', LoginAPIView.as_view()),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('login/', csrf_exempt(TokenObtainPairView.as_view()), name='token_obtain_pair'),
    path('api/token/refresh/', csrf_exempt(TokenRefreshView.as_view()), name='token_refresh'),
    path('api/token/verify/', csrf_exempt(TokenVerifyView.as_view()), name='token_verify'),
    # path('subjects/<int:subject_id>/', )
]
