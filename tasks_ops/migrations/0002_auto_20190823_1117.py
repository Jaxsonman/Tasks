# Generated by Django 2.2.4 on 2019-08-23 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_ops', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managementlog',
            name='state',
            field=models.IntegerField(blank=True, choices=[(1, 'Starting'), (2, 'In Progress'), (3, 'Finished')], null=True),
        ),
    ]