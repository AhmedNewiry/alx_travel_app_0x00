from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    def get_permissions(self):
        """Allow read-only for unauthenticated users; require authentication for write operations."""
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        """Set host to current user on create."""
        serializer.save(host=self.request.user)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_permissions(self):
        """Require authentication for all actions."""
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        """Set user to current user on create."""
        serializer.save(user=self.request.user)