# Generated by Django 2.1.5 on 2020-04-28 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_gameitem_win_rate_change'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameitem',
            name='coins',
            field=models.IntegerField(default=200, verbose_name='Cчет'),
        ),
        migrations.AlterField(
            model_name='gameitem',
            name='win_rate_change',
            field=models.FloatField(default=4.0),
        ),
    ]
