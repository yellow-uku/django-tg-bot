# Generated by Django 3.2.13 on 2022-05-08 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0010_alter_contact_tg_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='tg_user',
        ),
        migrations.AddField(
            model_name='contact',
            name='username',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]