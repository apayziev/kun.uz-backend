from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

schema_view = get_schema_view(title="Kun.uz API")

schema_view_swagger = get_swagger_view(title="Kun.uz API")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("post.urls")),
    path("schema/", schema_view),
    path("docs/", include_docs_urls(title="Kun.uz API", description="Kun.uz API")),
    path("swagger-docs/", schema_view_swagger),
]
