# Generated by Django 4.2 on 2024-07-07 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='name')),
                ('logo', models.ImageField(upload_to='logo')),
                ('subtitle', models.TextField(max_length=1500)),
                ('call_us', models.CharField(max_length=75)),
                ('email_us', models.CharField(max_length=150)),
                ('phones', models.CharField(max_length=75)),
                ('address', models.TextField(max_length=250)),
                ('andriod_apps', models.URLField(blank=True, null=True)),
                ('ios_app', models.URLField(blank=True, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('youtube', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
