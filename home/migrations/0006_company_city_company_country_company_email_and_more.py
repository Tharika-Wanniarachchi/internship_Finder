# Generated by Django 5.0.2 on 2024-02-29 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_posttable_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='mobileNumber',
            field=models.TextField(blank=True, null=True),
        ),
    ]
