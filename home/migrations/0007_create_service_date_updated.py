# Generated by Django 4.0.3 on 2022-05-10 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_create_service_date_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='create_service',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
