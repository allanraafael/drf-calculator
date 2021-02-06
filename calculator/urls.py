from django.urls import path
from calculator import views

app_name = 'calculator'

urlpatterns = [
    path('operations/', views.OperationViewSet.as_view(), name='operations'),
    path('addition/', views.AdditionViewSet.as_view(), name='addition'),
    path('subtraction/', views.SubtractionViewSet.as_view(), name='subtraction'),
    path('multiplication/', views.MultiplicationViewSet.as_view(), name='multiplication'),
    path('floor-division/', views.FloorDivisionViewSet.as_view(), name='floor-division'),
]
