# Generated by Django 3.0.2 on 2020-01-21 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banana', '0007_user_chat_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additional',
            name='marriage',
            field=models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=3, null=True),
        ),
    ]
