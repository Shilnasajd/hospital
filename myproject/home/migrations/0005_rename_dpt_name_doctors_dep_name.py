# Generated by Django 4.1.1 on 2022-12-29 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_doc_name_booking_d_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctors',
            old_name='dpt_name',
            new_name='dep_name',
        ),
    ]
