# Generated by Django 3.2.19 on 2023-07-17 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Library', '0032_auto_20230717_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_status',
            field=models.CharField(choices=[('Published', 'Published'), ('Pending', 'Pending'), ('Rejected', 'Rejected')], default='Pending', max_length=9),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_status',
            field=models.CharField(choices=[('Unanswered', 'Unanswered'), ('Rejected', 'Rejected'), ('Answered', 'Answered')], default='Unanswered', max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_type',
            field=models.CharField(choices=[('M', 'Moderator'), ('A', 'Admin'), ('U', 'User')], default='U', max_length=1),
        ),
    ]
