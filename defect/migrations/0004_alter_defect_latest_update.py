# Generated by Django 4.2.11 on 2024-03-21 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defect', '0003_alter_defect_options_alter_defect_defect_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defect',
            name='latest_update',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
