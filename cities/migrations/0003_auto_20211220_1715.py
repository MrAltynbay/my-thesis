# Generated by Django 3.1.14 on 2021-12-20 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cities", "0002_auto_20211220_1712"),
    ]

    operations = [
        migrations.AlterField(
            model_name="city",
            name="name",
            field=models.CharField(max_length=50,
                                   unique=True, verbose_name="Город"),
        ),
    ]
