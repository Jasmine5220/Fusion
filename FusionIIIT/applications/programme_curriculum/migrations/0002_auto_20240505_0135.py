# Generated by Django 3.1.5 on 2024-05-05 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programme_curriculum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newproposalfile',
            name='is_archive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='proposal_tracking',
            name='receiver_archive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='proposal_tracking',
            name='sender_archive',
            field=models.BooleanField(default=False),
        ),
    ]
