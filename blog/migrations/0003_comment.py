# Generated by Django 4.1.7 on 2023-03-08 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_author_alter_post_slug_alter_post_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('comment_content', models.TextField(max_length=200)),
                ('date', models.DateField(auto_now=True)),
                ('post_id', models.IntegerField()),
            ],
        ),
    ]