# Generated by Django 3.2.19 on 2023-07-14 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Library', '0021_auto_20230528_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_status',
            field=models.CharField(choices=[('Rejected', 'Rejected'), ('Published', 'Published'), ('Pending', 'Pending')], default='Pending', max_length=9),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_type',
            field=models.CharField(choices=[('U', 'User'), ('M', 'Moderator'), ('A', 'Admin')], default='U', max_length=1),
        ),
    ]
