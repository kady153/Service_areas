from django.contrib import admin
from django.urls import path, include
from geo import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Service_Area API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
   authentication_classes=[],
)

urlpatterns = [

    path('swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


    path('admin/', admin.site.urls),

    path('providers/',views.All_providers),

    path('provider/new/',views.New_provider),

    path('rest/pv_edit/<int:pk>',views.Provider_edit),

    path('areas/',views.SA_all),

    path('area/new/',views.Area_new),

    path('area/edit/<int:pk>',views.Area_edit),

    path('point_check/<str:lat>/<str:lng>',views.Point_check),

]
