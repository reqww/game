# Generated by Django 2.1.5 on 2020-04-29 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20200429_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameitem',
            name='choice',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gameitem',
            name='is_selected',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='gameitem',
            name='win_rate_change',
            field=models.FloatField(default=-0.5),
        ),
    ]