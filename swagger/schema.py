from django.urls import reverse
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


def get_schema():
    return get_schema_view(
        openapi.Info(
            title="Calculator API",
            default_version='v1',
            description="Desafio Pessoa Desenvolvedora (Python/Django) Backend",
            contact=openapi.Contact(email="allanrafaelfo@gmail.com"),
        ),
        public=False,
        permission_classes=[permissions.AllowAny],
    )
