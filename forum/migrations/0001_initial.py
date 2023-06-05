# Generated by Django 4.2.1 on 2023-06-05 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('commmentID', models.AutoField(primary_key=True, serialize=False)),
                ('parentID', models.IntegerField(default=0)),
                ('author', models.CharField(max_length=25)),
                ('content', models.TextField(max_length=2000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('postID', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=25)),
                ('title', models.TextField(max_length=60)),
                ('content', models.TextField(max_length=3000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
            ],
        ),
    ]