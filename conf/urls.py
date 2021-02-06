from django.urls import path, include


urlpatterns = [
    path('', include('swagger.urls')),
    path('calculator/', include('calculator.urls')),
]
