# Generated by Django 3.0.7 on 2020-11-18 12:07

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20201024_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='message',
            field=tinymce.models.HTMLField(verbose_name='Content Message'),
        ),
    ]
