# Generated by Django 5.0.3 on 2024-04-26 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_tbl_history_userid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_history',
        ),
    ]
