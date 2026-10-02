"""
SVCloud — Root URL configuration.

Routes:
    /api/          → API endpoints (from the api app)
    /api/schema/   → OpenAPI JSON/YAML schema (machine-readable)
    /api/docs/     → Swagger UI (human-readable, interactive)
"""

from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # Django admin (available but not our main interface)
    path("admin/", admin.site.urls),

    # ---------- API ----------
    path("api/", include("api.urls")),

    # ---------- OpenAPI / Swagger ----------
    # Machine-readable schema
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Interactive Swagger UI
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
