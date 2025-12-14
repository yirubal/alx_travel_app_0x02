from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth import get_user_model
from faker import Faker
import random

User = get_user_model()
fake = Faker()

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        if not users.exists():
            self.stdout.write(self.style.ERROR("No users found. Please create some users first."))
            return

        for _ in range(10):  # create 10 sample listings
            Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.text(),
                price_per_night=random.randint(50, 500),
                host=random.choice(users)
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded listings"))
