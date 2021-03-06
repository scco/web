# Generated by Django 2.2.4 on 2020-09-24 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0087_grantstat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grantstat',
            name='grant',
            field=models.ForeignKey(help_text='Grant to add stats for this grant', on_delete=django.db.models.deletion.CASCADE, related_name='stats', to='grants.Grant'),
        ),
    ]
