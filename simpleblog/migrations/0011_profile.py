# Generated by Django 5.1.5 on 2025-02-24 18:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleblog', '0010_blogmodel_likes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bio', models.TextField(null=True)),
                ('Image', models.ImageField(blank=True, default="{% static 'Media/Userprofile' %}", upload_to='')),
                ('Profileowner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userid', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
