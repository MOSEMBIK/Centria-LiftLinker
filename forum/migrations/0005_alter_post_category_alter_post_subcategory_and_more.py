# Generated by Django 4.2.1 on 2023-06-16 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_post_category_post_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='post',
            name='subcategory',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
