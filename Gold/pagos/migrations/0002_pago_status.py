# Generated by Django 4.2.7 on 2023-12-04 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]