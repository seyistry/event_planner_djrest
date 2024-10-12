from django.urls import path
from .views import (
    UpcomingEventListView,
    EventRegisterView,
    ManageWaitlistView,
    EventListCreateView,
    EventDetailView,
    UserCreateView,
    UserDetailView,
)

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('events/upcoming/', UpcomingEventListView.as_view(),
         name='upcoming-event-list'),
    path('events/<int:pk>/register/',
         EventRegisterView.as_view(), name='event-register'),
    path('events/<int:pk>/join-waitlist/',
         ManageWaitlistView.as_view(), name='join-waitlist'),
    path('users/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
