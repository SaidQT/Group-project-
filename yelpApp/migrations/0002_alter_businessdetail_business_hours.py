# Generated by Django 5.0.6 on 2024-05-26 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yelpApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessdetail',
            name='business_hours',
            field=models.CharField(default='', max_length=45),
        ),
    ]
