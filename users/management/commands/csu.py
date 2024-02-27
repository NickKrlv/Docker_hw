from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = 'Create superuser'

    def handle(self, *args, **options):
        admin = User.objects.create(
            email='admin@sky.pro',
            is_superuser=True,
            is_staff=True,
        )

        admin.set_password('5r36d6ft')
        admin.save()
        self.stdout.write(self.style.SUCCESS('Admin created'))
