# Generated by Django 4.1.2 on 2022-10-05 11:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('emailId', models.EmailField(max_length=254)),
                ('status', models.IntegerField(choices=[(0, 'UNSUBSCRIBED'), (1, 'SUBSCRIBED')], default=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
