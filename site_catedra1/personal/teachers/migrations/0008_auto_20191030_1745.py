# Generated by Django 2.2.6 on 2019-10-30 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0007_auto_20191030_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher_prof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('description', models.TextField(blank=True, max_length=11500, null=True)),
                ('image', models.ImageField(default=True, upload_to='personal/media/img/')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher_st_vikl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('description', models.TextField(blank=True, max_length=11500, null=True)),
                ('image', models.ImageField(default=True, upload_to='personal/media/img/')),
            ],
        ),
        migrations.RenameModel(
            old_name='Teacher',
            new_name='Teacher_dotsent',
        ),
    ]