# Generated by Django 4.0.3 on 2022-05-19 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_create_service_date_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_service',
            name='id',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]