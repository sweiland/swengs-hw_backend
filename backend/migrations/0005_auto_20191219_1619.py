# Generated by Django 3.0.1 on 2019-12-19 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_type_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.TextField(),
        ),
    ]
