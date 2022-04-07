# Generated by Django 4.0.3 on 2022-04-07 13:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_passport_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='Voter_ID',
            field=models.FileField(blank=True, upload_to='Documents/certificates/voter_id'),
        ),
        migrations.AlterField(
            model_name='passport',
            name='PAN',
            field=models.CharField(max_length=500, null=True, validators=[django.core.validators.RegexValidator('[A-Z]{5}[0-9]{4}[A-Z]{1}', message='Enter a Valid PAN Number')]),
        ),
    ]
