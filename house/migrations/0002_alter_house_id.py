# Generated by Django 5.1.1 on 2024-10-07 14:41

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b9413092-bf15-476d-9a24-fc194dfc585d'), editable=False, primary_key=True, serialize=False),
        ),
    ]
