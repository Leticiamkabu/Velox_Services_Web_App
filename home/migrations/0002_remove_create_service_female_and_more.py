# Generated by Django 4.0.3 on 2022-04-27 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='create_service',
            name='female',
        ),
        migrations.RemoveField(
            model_name='create_service',
            name='male',
        ),
        migrations.AlterField(
            model_name='create_service',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
