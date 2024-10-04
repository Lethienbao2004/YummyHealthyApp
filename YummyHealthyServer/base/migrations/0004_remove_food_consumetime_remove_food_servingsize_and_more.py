# Generated by Django 5.0 on 2024-01-06 06:27

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_servingsizeoption_servingsizefood_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='consumeTime',
        ),
        migrations.RemoveField(
            model_name='food',
            name='servingSize',
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('consumeTime', models.DateTimeField(auto_now=True)),
                ('numServings', models.IntegerField()),
                ('servingSizeOption', models.CharField(max_length=50, null=True)),
                ('servingSizeOptionMultiplier', models.FloatField()),
                ('food', models.ForeignKey(default= "71a9e805-de6d-42da-ad20-f4173c54ed8c",on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='base.food')),
            ],
        ),
    ]
