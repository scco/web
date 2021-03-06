# Generated by Django 2.2.20 on 2021-04-28 04:59

import app.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quadraticlands', '0006_qlvote_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='gtcsteward',
            name='custom_steward_img',
            field=models.ImageField(blank=True, help_text='override steward image as opposed to profile avatar', null=True, upload_to=app.utils.get_upload_filename),
        ),
    ]
