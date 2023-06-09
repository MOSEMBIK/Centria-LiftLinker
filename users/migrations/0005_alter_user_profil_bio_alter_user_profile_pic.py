# Generated by Django 4.2.1 on 2023-06-14 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_favorite_user_profil_bio_user_profile_pic_user_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profil_bio',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default=None, upload_to='profile_pics'),
        ),
    ]
