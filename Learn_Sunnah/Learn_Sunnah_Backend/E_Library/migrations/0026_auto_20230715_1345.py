# Generated by Django 3.2.19 on 2023-07-15 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Library', '0025_auto_20230715_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_status',
            field=models.CharField(choices=[('Rejected', 'Rejected'), ('Published', 'Published'), ('Pending', 'Pending')], default='Pending', max_length=9),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_status',
            field=models.CharField(choices=[('Answered', 'Answered'), ('Unanswered', 'Unanswered'), ('Rejected', 'Rejected')], default='Unanswered', max_length=10),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], default='Private', max_length=7),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_type',
            field=models.CharField(choices=[('A', 'Admin'), ('U', 'User'), ('M', 'Moderator')], default='U', max_length=1),
        ),
    ]
