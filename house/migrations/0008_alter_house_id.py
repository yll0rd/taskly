# Generated by Django 5.1.1 on 2024-10-10 13:46

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0007_alter_house_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4408b826-243d-480b-8c2e-0df001f7c97e'), editable=False, primary_key=True, serialize=False),
        ),
    ]
