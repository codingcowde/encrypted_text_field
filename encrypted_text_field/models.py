from django.db import models
from cryptography.fernet import Fernet
from django.conf import settings
from encrypted_text_field.forms import EncryptedTextFormField  # Assume the form field is in forms.py

class EncryptedTextField(models.Field):
    def get_internal_type(self):
        return "TextField"

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        try:
            key = settings.ENCRYPTION_KEY.encode()
            f = Fernet(key)
            decrypted_value = f.decrypt(value.encode()).decode()
            return decrypted_value
        except Exception as e:
            # Log the exception
            return None

    def to_python(self, value):
        if isinstance(value, str):
            return value
        if value is None:
            return value

    def get_prep_value(self, value):
        try:
            key = settings.ENCRYPTION_KEY.encode()
            f = Fernet(key)
            encrypted_value = f.encrypt(value.encode())
            return encrypted_value.decode()
        except Exception as e:
            return None

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)

    def formfield(self, **kwargs):
        # Return an instance of the custom form field with default parameters merged with any additional parameters
        defaults = {'form_class': EncryptedTextFormField}
        defaults.update(kwargs)
        return super().formfield(**defaults)
