# Generated by Django 5.0.3 on 2024-03-31 08:48

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '__first__'),
        ('major', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('personal_introduction', models.CharField(max_length=2000)),
                ('company_address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='company_address', to='base.address')),
                ('major', models.ManyToManyField(to='major.major')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]