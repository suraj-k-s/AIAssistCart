# Generated by Django 5.0.3 on 2024-04-26 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0004_tbl_seller'),
        ('User', '0010_delete_tbl_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_history', models.CharField(max_length=50)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
