# Generated by Django 3.2.19 on 2023-07-21 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Library', '0047_auto_20230721_1927'),
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
    ]
