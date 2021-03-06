# Generated by Django 2.2.4 on 2020-11-21 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0162_auto_20201112_1639'),
        ('quests', '0028_auto_20201109_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='reward_tip',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quests_reward_token', to='dashboard.Tip'),
        ),
    ]
