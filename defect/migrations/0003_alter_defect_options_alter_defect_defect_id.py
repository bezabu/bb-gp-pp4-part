# Generated by Django 4.2.11 on 2024-03-21 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defect', '0002_defect'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='defect',
            options={'ordering': ['-reported_on']},
        ),
        migrations.AlterField(
            model_name='defect',
            name='defect_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]