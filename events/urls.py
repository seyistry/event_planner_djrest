from django.urls import path
from .views import (
    UpcomingEventListView,
    EventRegisterView,
    JoinWaitListView,
    EventListCreateView,
    EventDetailView,
    UserCreateView,
    UserDetailView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('events/upcoming/', UpcomingEventListView.as_view(),
         name='upcoming-event-list'),
    path('events/<int:pk>/register/',
         EventRegisterView.as_view(), name='event-register'),
    path('events/<int:pk>/join-waitlist/',
         JoinWaitListView.as_view(), name='join-waitlist'),
    path('users/', UserCreateView.as_view(), name='user-create'),
    path('users/info/', UserDetailView.as_view(), name='user-detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
