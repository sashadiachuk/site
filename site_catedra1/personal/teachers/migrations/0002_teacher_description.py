# Generated by Django 2.2.6 on 2019-10-29 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
