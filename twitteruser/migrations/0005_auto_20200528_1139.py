# Generated by Django 3.0.6 on 2020-05-28 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0004_auto_20200528_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitteruser',
            name='display_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]