from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, filters, pagination, status
from rest_framework.response import Response
from .serializers import (
    EventSerializer,
    UserSerializer,
    EventRegistrationSerializer
)
from .permissions import IsOwnerOrReadOnly
from .models import Event
from django_filters.rest_framework import DjangoFilterBackend
from .filters import EventFilter
from django.utils import timezone

User = get_user_model()


class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    # List events but filter only for the authenticated user's events
    def get_queryset(self):
        return Event.objects.filter(organizer=self.request.user)


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class EventRegisterView(generics.GenericAPIView):
    queryset = Event.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EventRegistrationSerializer

    def get_object(self):
        """Retrieve the event instance."""
        try:
            return Event.objects.get(pk=self.kwargs['pk'])
        except Event.DoesNotExist:
            return Response({"detail": "Event not found."}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        """Allow a user to register for an event."""
        event = self.get_object()
        if isinstance(event, Response):  # Check if the event retrieval returned a Response
            return event

        # Check if the user is already attending
        if request.user in event.attendees.all():
            return Response({"detail": "You are already registered for this event."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the user is already on the waitlist
        if request.user in event.waitlist.all():
            return Response({"detail": "You are already on the waitlist for this event."}, status=status.HTTP_400_BAD_REQUEST)

        # If the event is not full
        if not event.is_full():
            return Response({"detail": event.title, "capacity_left": event.capacity - event.attendees.count()}, status=status.HTTP_200_OK)

        # If the event is full
        return Response({"detail": "The event is full"}, status=status.HTTP_200_OK)

    def post(self, request, pk):
        """Allow a user to register for an event."""
        event = self.get_object()
        if isinstance(event, Response):  # Check if the event retrieval returned a Response
            return event

        # Check if the user is already attending
        if request.user in event.attendees.all():
            return Response({"detail": "You are already registered for this event."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the user is already on the waitlist
        if request.user in event.waitlist.all():
            return Response({"detail": "You are already on the waitlist for this event."}, status=status.HTTP_400_BAD_REQUEST)

        # If the event is not full, add the user as an attendee
        if not event.is_full():
            event.attendees.add(request.user)
            return Response({"detail": "You have successfully registered for the event."}, status=status.HTTP_200_OK)

        # If the event is full
        return Response({"detail": "The event is full"}, status=status.HTTP_200_OK)


class JoinWaitListView(generics.GenericAPIView):
    queryset = Event.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EventRegistrationSerializer

    def post(self, request, pk):
        """Allow a user to register for an event."""
        event = self.get_object()
        # Check if the user is already attending
        if request.user in event.attendees.all():
            return Response({"detail": "You are already registered for this event."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the user is already on the waitlist
        if request.user in event.waitlist.all():
            return Response({"detail": "You are already on the waitlist for this event."}, status=status.HTTP_400_BAD_REQUEST)

        # If the event is not full, add the user as an attendee
        if not event.is_full():
            event.attendees.add(request.user)
            return Response({"detail": "You have successfully registered for the event."}, status=status.HTTP_200_OK)

        # If the event is full, add the user to the waitlist
        event.waitlist.add(request.user)
        return Response({"detail": "The event is full. You have been added to the waitlist."}, status=status.HTTP_200_OK)


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to register

# View for user details, updates, and deletion


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Ensure users can only manage their own account
    def get_object(self):
        return self.request.user


class UpcomingEventListPagination(pagination.PageNumberPagination):
    page_size = 10  # Customize page size if needed
    page_size_query_param = 'page_size'  # Allow client to set page size
    max_page_size = 100  # Set a maximum page size to prevent abuse


class UpcomingEventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = EventFilter
    ordering_fields = ['date_time']  # Allows ordering by event date
    ordering = ['date_time']  # Default ordering
    pagination_class = UpcomingEventListPagination  # Use custom pagination

    # Override the queryset to only include upcoming events
    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter out events that have already occurred
        return queryset.filter(date_time__gte=timezone.now())
