# Generated by Django 4.0.3 on 2022-06-07 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_auto_20220603_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mydata',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
