# Generated by Django 4.0.10 on 2023-07-05 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fleets', '0015_alter_evefleet_fleet_commander_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EveFleetDiscordWebhook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('webhook_url', models.CharField(max_length=255, unique=True)),
                ('audience', models.CharField(choices=[('militia', 'Militia'), ('alliance', 'Alliance'), ('academy', 'Academy')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EveFleetDiscordNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('created', 'Created'), ('preping', 'Preping'), ('ping', 'Ping')], max_length=255)),
                ('fleet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fleets.evefleet')),
            ],
            options={
                'unique_together': {('type', 'fleet')},
            },
        ),
    ]
