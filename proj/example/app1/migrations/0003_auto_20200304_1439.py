# Generated by Django 2.2.5 on 2020-03-04 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20200304_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='is_user_value',
            field=models.BinaryField(default=False),
        ),
    ]
