# Generated by Django 2.2.5 on 2019-11-11 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0007_auto_20191111_1108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='house_rulues',
            new_name='house_rules',
        ),
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to='room_photos'),
        ),
    ]
