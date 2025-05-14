from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Barter API",
        default_version="v1",
        description="Документация API для платформы обмена вещами",
        contact=openapi.Contact(email="karina.apaeva96@gmail.com"),
        license=openapi.License(name="MIT License")
    ),
    public=True,
    permission_classes=[permissions.AllowAny],

)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("ads.urls")),  # HTML
    path("api/", include("ads.api_urls")),  # API
    path("api-auth/", include("rest_framework.urls")),  # для логина в API
    path("api/auth/", include("djoser.urls")),
    path("api/auth", include("djoser.urls.jwt")),

    path("swagger/", schema_view.with_ui("swagger",
         cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc",
         cache_timeout=0), name="schema-redoc"),

]
