# Generated by Django 3.2.19 on 2023-07-17 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Library', '0029_auto_20230717_0907'),
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
            field=models.CharField(choices=[('Unanswered', 'Unanswered'), ('Answered', 'Answered'), ('Rejected', 'Rejected')], default='Unanswered', max_length=10),
        ),
    ]
