# Generated by Django 3.2.5 on 2021-07-11 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annotator', '0012_page1_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page1',
            old_name='text',
            new_name='anno',
        ),
    ]