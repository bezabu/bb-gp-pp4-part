# Generated by Django 4.2.11 on 2024-03-23 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defect', '0007_update'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='update',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterField(
            model_name='update',
            name='update_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
