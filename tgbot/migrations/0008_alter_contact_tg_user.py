# Generated by Django 3.2.13 on 2022-05-07 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0007_contact_tg_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='tg_user',
            field=models.CharField(default=False, max_length=32),
        ),
    ]
