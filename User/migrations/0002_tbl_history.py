# Generated by Django 5.0.3 on 2024-04-25 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_history', models.CharField(max_length=50)),
            ],
        ),
    ]
