# Generated by Django 5.0 on 2024-01-02 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servingsizeoption',
            name='multiplier',
            field=models.FloatField(default=2.0),
            preserve_default=False,
        ),
    ]
