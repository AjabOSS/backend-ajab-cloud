# Generated by Django 4.2.6 on 2023-10-19 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0002_alter_myuser_username_emailconfirmationtoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailconfirmationtoken',
            name='code',
            field=models.IntegerField(default=265563),
        ),
    ]