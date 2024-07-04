# Generated by Django 4.2 on 2024-07-03 17:22

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='name')),
                ('image', models.ImageField(upload_to='photo_brand')),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='name')),
                ('flag', models.CharField(choices=[('New', 'New'), ('Sale', 'Sale'), ('Feature', 'Feature')], max_length=50)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='photo_image')),
                ('sku', models.IntegerField()),
                ('subtitle', models.TextField(max_length=5000)),
                ('descriptions', models.TextField(max_length=50000)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('quantity', models.FloatField()),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_brand', to='products.brand')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productimage_product', to='products.product')),
            ],
        ),
    ]
