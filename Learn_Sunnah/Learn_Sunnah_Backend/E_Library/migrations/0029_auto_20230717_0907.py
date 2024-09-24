# Generated by Django 3.2.19 on 2023-07-17 09:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('E_Library', '0028_auto_20230715_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='rank',
        ),
        migrations.AlterField(
            model_name='book',
            name='book_status',
            field=models.CharField(choices=[('Rejected', 'Rejected'), ('Published', 'Published'), ('Pending', 'Pending')], default='Pending', max_length=9),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_status',
            field=models.CharField(choices=[('Unanswered', 'Unanswered'), ('Rejected', 'Rejected'), ('Answered', 'Answered')], default='Unanswered', max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_type',
            field=models.CharField(choices=[('A', 'Admin'), ('M', 'Moderator'), ('U', 'User')], default='U', max_length=1),
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(choices=[(1, 'Upvote'), (-1, 'Downvote')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_Library.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
