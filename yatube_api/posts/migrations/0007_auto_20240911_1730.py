# Generated by Django 3.2.16 on 2024-09-11 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20240911_1726'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='Unique user follow',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='Unique_user_follow'),
        ),
    ]
