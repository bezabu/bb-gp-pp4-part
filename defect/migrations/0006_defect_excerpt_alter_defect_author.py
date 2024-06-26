# Generated by Django 4.2.11 on 2024-03-22 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('defect', '0005_alter_defect_reoccurance_alter_defect_updates_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='defect',
            name='excerpt',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='defect',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='defects', to=settings.AUTH_USER_MODEL),
        ),
    ]
