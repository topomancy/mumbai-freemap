from django.core.management.base import BaseCommand
from cts import import_stable

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        import_stable.import_stables()
