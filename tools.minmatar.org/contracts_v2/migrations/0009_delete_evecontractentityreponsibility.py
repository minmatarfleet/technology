# Generated by Django 4.1.5 on 2023-03-12 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contracts_v2', '0008_evecontractexpectation_entities_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EveContractEntityReponsibility',
        ),
    ]