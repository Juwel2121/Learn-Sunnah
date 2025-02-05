# Generated by Django 3.2.19 on 2023-07-21 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Library', '0035_auto_20230717_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_status',
            field=models.CharField(choices=[('Published', 'Published'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], default='Pending', max_length=9),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_status',
            field=models.CharField(choices=[('Unanswered', 'Unanswered'), ('Rejected', 'Rejected'), ('Answered', 'Answered')], default='Unanswered', max_length=10),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('Private', 'Private'), ('Public', 'Public')], default='Private', max_length=7),
        ),
    ]
