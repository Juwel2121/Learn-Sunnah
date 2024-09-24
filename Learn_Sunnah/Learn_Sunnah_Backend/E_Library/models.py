from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator

PROFILE_ADMIN = 'A'
PROFILE_MODERATOR = 'M'
PROFILE_USER = 'U'
PROFILE_CHOICES = {
        (PROFILE_ADMIN, 'Admin'),
        (PROFILE_MODERATOR, 'Moderator'),
        (PROFILE_USER, 'User'),
    }

STATUS_PENDING = 'Pending'
STATUS_PUBLISHED = 'Published'
STATUS_REJECTED = 'Rejected'
STATUS_CHOICES = {
        (STATUS_PENDING, STATUS_PENDING),
        (STATUS_PUBLISHED, STATUS_PUBLISHED),
        (STATUS_REJECTED, STATUS_REJECTED),
    }


QUESTION_UNANSWERED = 'Unanswered'
QUESTION_ANSWERED = 'Answered'
QUESTION_REJECTED = 'Rejected'
QUESTION_CHOICES = {
        (QUESTION_UNANSWERED, QUESTION_UNANSWERED),
        (QUESTION_ANSWERED, QUESTION_ANSWERED),
        (QUESTION_REJECTED, QUESTION_REJECTED),
    }

QUESTION_TYPE_PUBLIC = 'Public'
QUESTION_TYPE_PRIVATE = 'Private'
QUESTION_TYPE_CHOICES = {
        (QUESTION_TYPE_PUBLIC, QUESTION_TYPE_PUBLIC),
        (QUESTION_TYPE_PRIVATE, QUESTION_TYPE_PRIVATE),
    }

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(unique=True)
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    phone = models.CharField(max_length=12)
    birth_date = models.DateField(null=True, blank=True)
    profile_type = models.CharField(
        max_length=1, choices=PROFILE_CHOICES, default=PROFILE_USER
    )

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'
    
    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name
    
    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name
    
    class Meta:
        ordering = ['user__first_name', 'user__last_name']


class BookCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    isbn = models.CharField(max_length=100, blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    publish_date = models.DateField(blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)
    page_number = models.PositiveIntegerField(default=0, blank=True, null=True)
    cover_photo = models.ImageField(upload_to='cover_photos', blank=True, null=True)
    pdf = models.FileField(upload_to='pdfs', blank=True, null=True, 
        validators=[
            FileExtensionValidator(allowed_extensions=['pdf'])
        ]
    )
    book_status = models.CharField(
        max_length=9, choices=STATUS_CHOICES, default=STATUS_PENDING
    )
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, related_name='books')

    def __str__(self) -> str:
        return self.name
    

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    date_time = models.DateTimeField(auto_now=True)
    review = models.TextField(blank=True, null=True)
    
    class Meta:
        unique_together = ('user', 'book')

    def __str__(self) -> str:
        return self.review


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='ratings')
    date_time = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(blank=False, null=False, validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
    ])

    class Meta:
        unique_together = ('user', 'book')

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name} - {self.rating}'


class QuestionCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Question(models.Model):
    question = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    category = models.ForeignKey(QuestionCategory, on_delete=models.CASCADE, related_name='questions')
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=100, blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    answer_photo = models.ImageField(upload_to='answer/photos', blank=True, null=True)
    answer_video = models.FileField(upload_to='answer/videos', blank=True, null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['mp4', 'webm', 'ogg'])
        ]
    )
    question_status = models.CharField(
        max_length=10, choices=QUESTION_CHOICES, default=QUESTION_UNANSWERED
    )
    question_type = models.CharField(
        max_length=7, choices=QUESTION_TYPE_CHOICES, default=QUESTION_TYPE_PRIVATE
    )

    def __str__(self) -> str:
        return f'{self.question} | {self.author.username}' 
    

class Comment(models.Model):
    comment = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='comments')

 
class Reply(models.Model):
    reply = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')


class Rank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ranks')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='ranks')
    value = models.IntegerField(choices=((1, 'Upvote'), (-1, 'Downvote')))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta():
        unique_together = ('user', 'question')