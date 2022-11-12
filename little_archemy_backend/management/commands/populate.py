from django.core.management.base import BaseCommand, CommandError
from archemy.domain.queries import Populate

class Command(BaseCommand):
    help = 'help text'

    def handle(self, *args, **options):
        Populate().populate()
        self.stdout.write("La base de datos ha sido poblada")
