# Generated by Django 4.1.3 on 2022-11-13 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_user_options_news'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-added_at']},
        ),
    ]
