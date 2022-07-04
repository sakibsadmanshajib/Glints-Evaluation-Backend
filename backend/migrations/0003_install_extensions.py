from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('backend', '0002_auto_20220628_2329'),
    ]

    operations = [
        TrigramExtension(),
    ]