# Generated by Django 4.2.1 on 2023-06-15 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.TextField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='post',
            name='subcategory',
            field=models.TextField(default='', max_length=60),
        ),
    ]