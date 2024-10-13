from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import Event

User = get_user_model()


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date_time',
                  'location', 'capacity', 'organizer', 'created_date']
        read_only_fields = ['organizer', 'created_date']

    date_time = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S%z")

    def create(self, validated_data):
        # Set the organizer to the current user
        validated_data['organizer'] = self.context['request'].user
        return super().create(validated_data)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        # Create a new user and hash their password
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        # Update user data and hash the password if provided
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class EventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = []  # You can include relevant fields here if needed