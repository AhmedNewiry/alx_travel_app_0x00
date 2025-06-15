from django.core.management.base import BaseCommand
from django.utils import timezone
from listings.models import User, Listing, Booking, Review
import uuid
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Seeds the database with sample listings data'

    def handle(self, *args, **kwargs):
        # Create users
        host = User.objects.create_user(
            user_id=uuid.uuid4(),
            username='host1',
            email='host1@example.com',
            password='pass123',
            first_name='John',
            last_name='Doe',
            role='host'
        )
        guest = User.objects.create_user(
            user_id=uuid.uuid4(),
            username='guest1',
            email='guest1@example.com',
            password='pass123',
            first_name='Jane',
            last_name='Smith',
            role='guest'
        )

        # Create listings
        listing1 = Listing.objects.create(
            property_id=uuid.uuid4(),
            host=host,
            name='Cozy Cabin',
            description='A cozy cabin in the woods',
            location='Mountain Town',
            pricepernight=100.00
        )
        listing2 = Listing.objects.create(
            property_id=uuid.uuid4(),
            host=host,
            name='Beach House',
            description='A beautiful beachfront property',
            location='Coastal City',
            pricepernight=150.00
        )

        # Create bookings
        today = timezone.now().date()
        Booking.objects.create(
            booking_id=uuid.uuid4(),
            property=listing1,
            user=guest,
            start_date=today + timedelta(days=1),
            end_date=today + timedelta(days=3),
            status='confirmed'
        )
        Booking.objects.create(
            booking_id=uuid.uuid4(),
            property=listing2,
            user=guest,
            start_date=today + timedelta(days=5),
            end_date=today + timedelta(days=7),
            status='pending'
        )

        # Create reviews
        Review.objects.create(
            review_id=uuid.uuid4(),
            property=listing1,
            user=guest,
            rating=5,
            comment='Amazing stay!'
        )
        Review.objects.create(
            review_id=uuid.uuid4(),
            property=listing2,
            user=guest,
            rating=4,
            comment='Great location, but needs better Wi-Fi'
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded database with sample data'))