# Generated by Django 4.0.10 on 2023-07-06 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleets', '0016_evefleetdiscordwebhook_evefleetdiscordnotification'),
    ]

    operations = [
        migrations.AddField(
            model_name='evefleetdiscordwebhook',
            name='name',
            field=models.CharField(default='Unknown', max_length=255),
            preserve_default=False,
        ),
    ]
