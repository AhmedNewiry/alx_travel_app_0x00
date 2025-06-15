from rest_framework import serializers
from .models import Listing, Booking, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'first_name', 'last_name', 'role']

class ListingSerializer(serializers.ModelSerializer):
    host = UserSerializer(read_only=True)
    class Meta:
        model = Listing
        fields = ['property_id', 'host', 'name', 'description', 'location', 'pricepernight', 'created_at', 'updated_at']

class BookingSerializer(serializers.ModelSerializer):
    property = ListingSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Booking
        fields = ['booking_id', 'property', 'user', 'start_date', 'end_date', 'status', 'created_at']