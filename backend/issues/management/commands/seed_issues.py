from django.core.management.base import BaseCommand
from issues.models import Issue
from django.contrib.auth import get_user_model
import random

class Command(BaseCommand):
    help = 'Seed the database with demo issues'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        users = User.objects.all()

        if not users.exists():
            self.stdout.write(self.style.ERROR("No users found. Please create a user first."))
            return

        severities = ["low", "medium", "high"]

        for i in range(10):
            Issue.objects.create(
                title=f"Issue {i+1}",
                description="This is a seeded issue.",
                severity=random.choice(severities),
                created_by=random.choice(users),  # ✅ correct field name
            )

        self.stdout.write(self.style.SUCCESS("Demo issues created successfully."))
