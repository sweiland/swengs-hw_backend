# Generated by Django 3.0.2 on 2020-01-05 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20191219_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Type'),
        ),
        migrations.AlterField(
            model_name='member',
            name='friends',
            field=models.ManyToManyField(related_name='_member_friends_+', to='backend.Member'),
        ),
    ]
