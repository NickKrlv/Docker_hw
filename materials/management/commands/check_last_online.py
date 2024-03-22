from django.core.management import BaseCommand

from materials.tasks import check_last_online


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        check_last_online()
