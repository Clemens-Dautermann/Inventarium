# Generated by Django 2.1.4 on 2018-12-22 19:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('object_adder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.TextField(max_length=150)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]