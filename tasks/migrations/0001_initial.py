# Generated by Django 2.2.4 on 2019-08-23 16:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('current_bid', models.FloatField()),
                ('bid_count', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('live_date', models.DateTimeField()),
                ('expiry_date', models.DateTimeField()),
                ('active', models.BooleanField()),
                ('owner', models.ForeignKey(on_delete=None, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('email_sent', models.BooleanField(default=False)),
                ('email_sent_time', models.DateTimeField(blank=True, null=True)),
                ('auction', models.ForeignKey(on_delete=None, to='tasks.Auction')),
                ('owner', models.ForeignKey(on_delete=None, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmailQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.DateField()),
                ('auction', models.ForeignKey(blank=True, null=True, on_delete=None, to='tasks.Auction')),
                ('bid', models.ForeignKey(blank=True, null=True, on_delete=None, to='tasks.Bid')),
            ],
        ),
    ]
