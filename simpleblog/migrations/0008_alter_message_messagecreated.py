# Generated by Django 5.1.5 on 2025-02-12 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleblog', '0007_rename_created_message_messagecreated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='messageCreated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
