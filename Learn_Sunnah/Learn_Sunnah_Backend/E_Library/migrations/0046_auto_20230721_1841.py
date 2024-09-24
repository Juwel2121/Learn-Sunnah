# Generated by Django 3.2.19 on 2023-07-21 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('E_Library', '0045_auto_20230721_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='book_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Published', 'Published'), ('Rejected', 'Rejected')], default='Pending', max_length=9),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_status',
            field=models.CharField(choices=[('Answered', 'Answered'), ('Unanswered', 'Unanswered'), ('Rejected', 'Rejected')], default='Unanswered', max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_type',
            field=models.CharField(choices=[('A', 'Admin'), ('M', 'Moderator'), ('U', 'User')], default='U', max_length=1),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to=settings.AUTH_USER_MODEL)),
                ('reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='E_Library.comment')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='E_Library.question'),
        ),
    ]
