# Generated by Django 5.1.6 on 2025-02-23 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_blog_created_at_alter_blog_rich_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фотогалерея',
            },
        ),
    ]
