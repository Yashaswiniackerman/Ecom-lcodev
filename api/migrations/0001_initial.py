from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="yashaswini",
        email ="kyyashaswini27@gmail.com",
        is_staff=True,
        is_superuser=True,
        phone="987654321",
        gender="Female")

        user.set_password("1234567890")
        user.save()

    dependencies =[

    ]
    
    operations = [
        migrations.RunPython(seed_data),
    ]