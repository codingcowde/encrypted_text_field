from django import forms
from django.conf import settings

class EncryptedTextFormField(forms.CharField):
    widget = forms.PasswordInput(render_value=False)

    def __init__(self, *args, **kwargs):
        # Check if the encryption key is present in settings
        if not hasattr(settings, 'ENCRYPTION_KEY') or not settings.ENCRYPTION_KEY:
            default_help_text = "No encryption key is configured in settings."
        else:
            # Use default help_text if it's provided, otherwise use an empty string
            default_help_text = kwargs.get('help_text', '')

        # Update the help_text keyword argument
        kwargs['help_text'] = default_help_text

        super().__init__(*args, **kwargs)

    def prepare_value(self, value):
        # Since we don't want to show the decrypted value, always return None
        return None
