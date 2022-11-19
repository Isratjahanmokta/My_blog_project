# Generated by Django 4.0.4 on 2022-11-16 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_blog', '0003_alter_blog_blog_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='Comment',
            new_name='comment',
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_image',
            field=models.ImageField(upload_to='blog_image', verbose_name='Image'),
        ),
    ]