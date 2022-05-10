# Generated by Django 4.0.4 on 2022-05-10 09:05

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default=None, force_format=None, keep_meta=True, null=True, quality=85, size=[500, 300], upload_to='images/%Y/%m/%d/'),
        ),
    ]
