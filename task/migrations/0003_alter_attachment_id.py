# Generated by Django 5.1.1 on 2024-10-09 20:34

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_attachment_tasklist_task_task_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='id',
            field=models.UUIDField(default=uuid.UUID('6b13ffcf-7d5e-4620-9e72-6bac20067652'), editable=False, primary_key=True, serialize=False),
        ),
    ]
