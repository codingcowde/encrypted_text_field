# encrypted_text_field Django App

`encrypted_text_field` is a Django app providing a custom model field for storing sensitive information like passwords and API keys. The data is encrypted before being saved to the database and decrypted when accessed through Django's ORM in views or other business logic. The field will be rendered in Django's admin but ensures that values are not readable or displayed back in the UI, protecting sensitive information from exposure.

## Features

- **EncryptedTextField Model Field**: Encrypt and decrypt data automatically.
- **Security in Django Admin**: Displays a password widget in the admin interface to edit fields without showing existing values.
- **Generate Keys via Management Command**: Includes a Django management command to generate new encryption keys.

## Requirements

- Django 3.2 or newer
- Cryptography

## Intallation using PIP

```bash
pip install encrypted-text-field
```

## Installation via GitHub

Follow these steps to install and use the `encrypted_text_field` in your Django project:


1. **Install the package**

   Clone this repository into an empty folder within your Django project directory:

   ```bash
   git clone https://github.com/codingcowde/encrypted_text_field.git
   ```

## Setup
1. **Add `encrypted_text_field` to your `INSTALLED_APPS`**

   ```python
   INSTALLED_APPS = [
       ...
       'encrypted_text_field',
       ...
   ]
   ```

2. **Configure the Encryption Key**

   In your settings module, set the encryption key:

   ```python
   ENCRYPTION_KEY = 'your_generated_encryption_key_here'
   ```

   > **Note**: This key should be generated securely and kept secret. Use environment variables to manage keys securely in production.

3. **Run Migrations**

   ```bash
   python manage.py migrate
   ```

## Usage

To use `EncryptedTextField` in your models:

```python
from django.db import models
from encrypted_text_field.models import EncryptedTextField

class MyModel(models.Model):
    secret_data = EncryptedTextField()
```

## Admin Interface

In the admin interface, `EncryptedTextField` will appear as a password input. The actual data is never displayed in the admin to prevent leakage of sensitive information.

## Generating a New Encryption Key

Run the following management command to generate a new encryption key:

```bash
python manage.py generate_encryption_key
```

Follow the instructions provided by the command output to replace your existing encryption key.

## Contributing

Contributions are welcome!

## License

Distributed under the MIT License. See `LICENSE` for more information.
