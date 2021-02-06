from django.urls import path

from conf.settings import CACHE_TTL
from swagger.schema import get_schema


app_name = 'swagger'
schema_view = get_schema()


urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=CACHE_TTL), name='schema-swagger-ui'),
]
