# Generated by Django 4.0.3 on 2022-05-19 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_create_service_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_service',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]