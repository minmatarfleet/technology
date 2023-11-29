# Generated by Django 4.1.5 on 2023-07-01 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contracts_v2', '0030_evecontract_fitting'),
        ('fleets', '0012_evedoctrine_primary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evefleet',
            name='motd',
        ),
        migrations.AddField(
            model_name='evefleet',
            name='audience',
            field=models.CharField(choices=[('militia', 'Militia'), ('alliance', 'Alliance'), ('academy', 'Academy')], default='militia', max_length=255),
        ),
        migrations.AddField(
            model_name='evefleet',
            name='doctrine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fleets.evedoctrine'),
        ),
        migrations.AddField(
            model_name='evefleet',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='evefleet',
            name='fleet_commander_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evefleet',
            name='fleet_commander_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evefleet',
            name='staging',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contracts_v2.evecontractlocation'),
        ),
        migrations.AddField(
            model_name='evefleet',
            name='start_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='evefleet',
            name='type',
            field=models.CharField(choices=[('frontline', 'Frontline'), ('structure', 'Structure'), ('roam', 'Roam'), ('stratop', 'Strategic Operation'), ('training', 'Training')], default='frontline', max_length=255),
        ),
    ]
