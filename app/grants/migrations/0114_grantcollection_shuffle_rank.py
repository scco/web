# Generated by Django 2.2.4 on 2021-03-09 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0113_grantapikey'),
    ]

    operations = [
        migrations.AddField(
            model_name='grantcollection',
            name='shuffle_rank',
            field=models.PositiveIntegerField(db_index=True, default=1),
        ),
    ]
