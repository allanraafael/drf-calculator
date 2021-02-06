from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics

from calculator import models, serializers
from conf.settings import CACHE_TTL


class OperationViewSet(generics.ListAPIView):
    queryset = models.Operation.objects.all()
    serializer_class = serializers.OperationSerializer

    @method_decorator(cache_page(CACHE_TTL))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class AdditionViewSet(generics.CreateAPIView):
    serializer_class = serializers.AdditionSerializer

    @method_decorator(cache_page(CACHE_TTL))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class SubtractionViewSet(generics.CreateAPIView):
    serializer_class = serializers.SubtractionSerializer

    @method_decorator(cache_page(CACHE_TTL))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class MultiplicationViewSet(generics.CreateAPIView):
    serializer_class = serializers.MultiplicationSerializer

    @method_decorator(cache_page(CACHE_TTL))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class FloorDivisionViewSet(generics.CreateAPIView):
    serializer_class = serializers.FloorDivisionSerializer

    @method_decorator(cache_page(CACHE_TTL))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
