# Generated by Django 4.1.5 on 2023-04-22 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='esicourierentityresponse',
            old_name='response',
            new_name='data',
        ),
        migrations.RenameField(
            model_name='esicourierentityresponse',
            old_name='courier_entity',
            new_name='entity',
        ),
    ]
