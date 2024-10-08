from django.urls import path
from .views import HotelViewSet, UserAPIVi





urlpatterns = [
    path('hotels/', HotelViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('hotels/<str:pk>/', HotelViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    # path('user/', UserAPIView.as_view()),
]