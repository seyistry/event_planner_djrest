from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Category(models.Model):
    class categoryChoice(models.TextChoices):
        MUSIC = 'Music'
        CONFERENCE = 'Conference'
        WORKSHOP = 'Workshop'
        CONCERT = 'Concert'
        SPORTS = 'Sports'
        ARTS = 'Arts'
        FOOD = 'Food'
        DRINKS = 'Drinks'
        CHARITY = 'Charity'
        EDUCATION = 'Education'
        BUSINESS = 'Business'
        TECH = 'Tech'
        OTHER = 'Other'

    name = models.CharField(
        max_length=100, choices=categoryChoice.choices, default=categoryChoice.OTHER)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)  # Optional description
    date_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField()
    attendees = models.ManyToManyField(
        User, related_name='attending_events', blank=True)
    waitlist = models.ManyToManyField(
        User, related_name='waitlisted_events', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(
        max_length=100, choices=Category.categoryChoice.choices, default=Category.categoryChoice.OTHER
    )

    def __str__(self):
        return self.title

    # Custom validation to prevent creating events with past dates
    def clean(self):
        if self.date_time < timezone.now():
            raise ValidationError(
                "You cannot create an event with a past date.")

    def is_full(self):
        """Check if the event has reached its maximum capacity."""
        return self.attendees.count() >= self.capacity

    def save(self, *args, **kwargs):
        # Ensure the clean method is called when saving through the ORM
        self.clean()
        super().save(*args, **kwargs)
