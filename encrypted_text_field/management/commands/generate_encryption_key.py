from django.core.management.base import BaseCommand
from cryptography.fernet import Fernet

class Command(BaseCommand):
    help = 'Generates a new encryption key'

    def handle(self, *args, **options):
        key = Fernet.generate_key()
        self.stdout.write(self.style.SUCCESS('Generated Key: {}'.format(key.decode())))
        self.stdout.write('WARNING: Changing the encryption key will cause loss of previously encrypted data. Set the new key in your settings file using the ENCRYPTION_KEY variable.')
