import django_filters
from .models import Event

class EventFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr='icontains')  # Case-insensitive search
    location = django_filters.CharFilter(field_name="location", lookup_expr='icontains')
    start_date = django_filters.DateFilter(field_name="date_time", lookup_expr='gte')  # Start of date range example 2024-01-01
    end_date = django_filters.DateFilter(field_name="date_time", lookup_expr='lte')    # End of date range example 2024-12-31

    class Meta:
        model = Event
        fields = ['title', 'location', 'start_date', 'end_date']
