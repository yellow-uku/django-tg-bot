# Generated by Django 3.2.13 on 2022-05-08 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0008_alter_contact_tg_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='tg_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tgbot.user'),
        ),
    ]