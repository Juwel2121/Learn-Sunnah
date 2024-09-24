# Generated by Django 3.2.19 on 2023-07-21 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Library', '0044_auto_20230721_1641'),
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
            field=models.CharField(choices=[('Rejected', 'Rejected'), ('Answered', 'Answered'), ('Unanswered', 'Unanswered')], default='Unanswered', max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_type',
            field=models.CharField(choices=[('A', 'Admin'), ('U', 'User'), ('M', 'Moderator')], default='U', max_length=1),
        ),
    ]