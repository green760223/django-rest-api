from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from myapp.views import LoginView, RegisterView, UserListView

schema_view = get_schema_view(
    openapi.Info(
        title="Djano REST APIs",
        default_version="v1",
        description="API documentation for Django REST APIs",
        contact=openapi.Contact(email="green760223@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("register", RegisterView.as_view(), name="register"),
    path("login", LoginView.as_view(), name="login"),
    path("users", UserListView.as_view(), name="user-list"),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
