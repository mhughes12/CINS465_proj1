# Generated by Django 2.2.5 on 2020-03-04 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='is_user_value',
            field=models.BinaryField(),
        ),
    ]
