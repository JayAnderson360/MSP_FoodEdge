# Generated by Django 2.2.14 on 2023-11-15 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190630_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Food 1'), ('SW', 'Food 2'), ('OW', 'Food 3')], max_length=2),
        ),
    ]
